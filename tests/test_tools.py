import json
import pytest
import respx
import httpx
from mcp.server.fastmcp import FastMCP
from app.client import HotpepperClient
from app.googleplace.client import GooglePlaceClient
from app.tools.gourmet import register_gourmet_tools
from app.tools.shop import register_shop_tools
from app.tools.masters import register_master_tools

BASE = "http://webservice.recruit.co.jp/hotpepper"
PLACES_BASE = "https://maps.googleapis.com/maps/api/place"

_TEXTSEARCH_OK = {"status": "OK", "results": [{"place_id": "ChIJtest123"}]}
_DETAIL_OK = {
    "status": "OK",
    "result": {
        "rating": 4.2,
        "opening_hours": {"open_now": True, "weekday_text": ["月曜日: 11:00～23:00"]},
    },
}
_REVIEWS_OK = {
    "status": "OK",
    "result": {
        "reviews": [
            {"author_name": "田中", "rating": 5, "text": "最高！", "relative_time_description": "1か月前"}
        ]
    },
}


@pytest.fixture
def client():
    return HotpepperClient(api_key="test_key")


def _make_gourmet_response(shops: list) -> dict:
    return {
        "results": {
            "api_version": "1.20",
            "results_available": len(shops),
            "results_returned": str(len(shops)),
            "results_start": 1,
            "shop": shops,
        }
    }


def _make_master_response(key: str, items: list) -> dict:
    return {
        "results": {
            "api_version": "1.20",
            "results_available": len(items),
            "results_returned": str(len(items)),
            "results_start": 1,
            key: items,
        }
    }


async def _call(mcp: FastMCP, tool_name: str, **kwargs) -> dict:
    content, _ = await mcp.call_tool(tool_name, kwargs)
    return json.loads(content[0].text)


# --- gourmet tools ---

@respx.mock
async def test_search_restaurants_keyword(client: HotpepperClient):
    respx.get(f"{BASE}/gourmet/v1/").mock(
        return_value=httpx.Response(200, json=_make_gourmet_response([
            {"id": "J000000001", "name": "銀座イタリアン"}
        ]))
    )
    mcp = FastMCP("test")
    register_gourmet_tools(mcp, client)

    result = await _call(mcp, "search_restaurants", keyword="イタリアン")
    assert result["shop"][0]["name"] == "銀座イタリアン"


@respx.mock
async def test_search_restaurants_with_filters(client: HotpepperClient):
    route = respx.get(f"{BASE}/gourmet/v1/").mock(
        return_value=httpx.Response(200, json=_make_gourmet_response([]))
    )
    mcp = FastMCP("test")
    register_gourmet_tools(mcp, client)

    await _call(mcp, "search_restaurants", keyword="焼肉", private_room=True, free_drink=True, count=5)
    url = str(route.calls.last.request.url)
    assert "private_room=1" in url
    assert "free_drink=1" in url
    assert "count=5" in url


@respx.mock
async def test_search_restaurants_course_and_card(client: HotpepperClient):
    route = respx.get(f"{BASE}/gourmet/v1/").mock(
        return_value=httpx.Response(200, json=_make_gourmet_response([]))
    )
    mcp = FastMCP("test")
    register_gourmet_tools(mcp, client)

    await _call(mcp, "search_restaurants", keyword="新宿", course=True, card=True)
    url = str(route.calls.last.request.url)
    assert "course=1" in url
    assert "card=1" in url


# --- shop tools ---

@respx.mock
async def test_search_shops(client: HotpepperClient):
    respx.get(f"{BASE}/shop/v1/").mock(
        return_value=httpx.Response(200, json={
            "results": {
                "api_version": "1.20",
                "results_available": 1,
                "results_returned": "1",
                "results_start": 1,
                "shop": [{"id": "J000000002", "name": "新宿カフェ"}],
            }
        })
    )
    mcp = FastMCP("test")
    register_shop_tools(mcp, client)

    result = await _call(mcp, "search_shops", keyword="新宿カフェ")
    assert result["shop"][0]["name"] == "新宿カフェ"


# --- master tools ---

@respx.mock
async def test_get_large_areas(client: HotpepperClient):
    respx.get(f"{BASE}/large_area/v1/").mock(
        return_value=httpx.Response(200, json=_make_master_response(
            "large_area", [{"code": "Z011", "name": "東京"}]
        ))
    )
    mcp = FastMCP("test")
    register_master_tools(mcp, client)

    result = await _call(mcp, "get_large_areas")
    assert result["large_area"][0]["code"] == "Z011"


@respx.mock
async def test_get_genres(client: HotpepperClient):
    respx.get(f"{BASE}/genre/v1/").mock(
        return_value=httpx.Response(200, json=_make_master_response(
            "genre", [{"code": "G001", "name": "居酒屋"}]
        ))
    )
    mcp = FastMCP("test")
    register_master_tools(mcp, client)

    result = await _call(mcp, "get_genres")
    assert result["genre"][0]["name"] == "居酒屋"


@respx.mock
async def test_get_budgets(client: HotpepperClient):
    respx.get(f"{BASE}/budget/v1/").mock(
        return_value=httpx.Response(200, json=_make_master_response(
            "budget", [{"code": "B001", "name": "～2000円"}]
        ))
    )
    mcp = FastMCP("test")
    register_master_tools(mcp, client)

    result = await _call(mcp, "get_budgets")
    assert result["budget"][0]["code"] == "B001"


# --- Google Places integration ---

@respx.mock
async def test_search_restaurants_with_google_client(client: HotpepperClient):
    respx.get(f"{BASE}/gourmet/v1/").mock(
        return_value=httpx.Response(200, json=_make_gourmet_response([
            {"id": "J000000001", "name": "テスト店", "address": "東京都新宿区"}
        ]))
    )
    respx.get(f"{PLACES_BASE}/textsearch/json").mock(
        return_value=httpx.Response(200, json=_TEXTSEARCH_OK)
    )
    respx.get(f"{PLACES_BASE}/details/json").mock(
        return_value=httpx.Response(200, json=_DETAIL_OK)
    )
    google_client = GooglePlaceClient(api_key="test_key")
    mcp = FastMCP("test")
    register_gourmet_tools(mcp, client, google_client)

    result = await _call(mcp, "search_restaurants", keyword="テスト")
    gp = result["shop"][0]["google_place"]
    assert gp["rating"] == 4.2
    assert gp["current_opening_hours"]["open_now"] is True
    assert "reviews" not in gp
    await google_client.aclose()


@respx.mock
async def test_get_restaurant_reviews(client: HotpepperClient):
    respx.get(f"{PLACES_BASE}/textsearch/json").mock(
        return_value=httpx.Response(200, json=_TEXTSEARCH_OK)
    )
    respx.get(f"{PLACES_BASE}/details/json").mock(
        return_value=httpx.Response(200, json=_REVIEWS_OK)
    )
    google_client = GooglePlaceClient(api_key="test_key")
    mcp = FastMCP("test")
    register_gourmet_tools(mcp, client, google_client)

    result = await _call(mcp, "get_restaurant_reviews", name="テスト店", address="東京都新宿区")
    assert result["name"] == "テスト店"
    assert result["reviews"][0]["author_name"] == "田中"
    assert result["reviews"][0]["rating"] == 5
    await google_client.aclose()


async def test_get_restaurant_reviews_no_google_client(client: HotpepperClient):
    mcp = FastMCP("test")
    register_gourmet_tools(mcp, client, google_client=None)

    result = await _call(mcp, "get_restaurant_reviews", name="テスト店", address="東京都新宿区")
    assert "error" in result
