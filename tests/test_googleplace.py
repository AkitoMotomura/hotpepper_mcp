import pytest
import respx
import httpx
from unittest.mock import AsyncMock

from app.googleplace.client import GooglePlaceClient
from app.googleplace.enricher import enrich_shops

PLACES_BASE = "https://maps.googleapis.com/maps/api/place"

_TEXTSEARCH_OK = {"status": "OK", "results": [{"place_id": "ChIJtest123"}]}
_DETAIL_OK = {
    "status": "OK",
    "result": {
        "rating": 4.2,
        "opening_hours": {
            "open_now": True,
            "weekday_text": ["月曜日: 11:00～23:00"],
        },
    },
}
_REVIEWS_OK = {
    "status": "OK",
    "result": {
        "reviews": [
            {
                "author_name": "田中太郎",
                "rating": 5,
                "text": "とても美味しかった",
                "relative_time_description": "1か月前",
            }
        ]
    },
}


@pytest.fixture
async def google_client():
    c = GooglePlaceClient(api_key="test_key")
    yield c
    await c.aclose()


# --- GooglePlaceClient.get_place_data ---

@respx.mock
async def test_get_place_data_returns_rating_and_opening_hours(google_client):
    respx.get(f"{PLACES_BASE}/textsearch/json").mock(
        return_value=httpx.Response(200, json=_TEXTSEARCH_OK)
    )
    respx.get(f"{PLACES_BASE}/details/json").mock(
        return_value=httpx.Response(200, json=_DETAIL_OK)
    )
    result = await google_client.get_place_data("テスト店", "東京都新宿区")
    assert result["rating"] == 4.2
    assert result["opening_hours"]["open_now"] is True


@respx.mock
async def test_get_place_data_zero_results(google_client):
    respx.get(f"{PLACES_BASE}/textsearch/json").mock(
        return_value=httpx.Response(200, json={"status": "ZERO_RESULTS", "results": []})
    )
    result = await google_client.get_place_data("存在しない店", "東京都")
    assert result == {}


@respx.mock
async def test_get_place_data_details_not_ok(google_client):
    respx.get(f"{PLACES_BASE}/textsearch/json").mock(
        return_value=httpx.Response(200, json=_TEXTSEARCH_OK)
    )
    respx.get(f"{PLACES_BASE}/details/json").mock(
        return_value=httpx.Response(200, json={"status": "NOT_FOUND", "result": {}})
    )
    result = await google_client.get_place_data("テスト店", "東京都新宿区")
    assert result == {}


# --- GooglePlaceClient.get_reviews ---

@respx.mock
async def test_get_reviews_returns_reviews(google_client):
    respx.get(f"{PLACES_BASE}/textsearch/json").mock(
        return_value=httpx.Response(200, json=_TEXTSEARCH_OK)
    )
    respx.get(f"{PLACES_BASE}/details/json").mock(
        return_value=httpx.Response(200, json=_REVIEWS_OK)
    )
    reviews = await google_client.get_reviews("テスト店", "東京都新宿区")
    assert len(reviews) == 1
    assert reviews[0]["author_name"] == "田中太郎"
    assert reviews[0]["rating"] == 5
    assert reviews[0]["text"] == "とても美味しかった"


@respx.mock
async def test_get_reviews_zero_results(google_client):
    respx.get(f"{PLACES_BASE}/textsearch/json").mock(
        return_value=httpx.Response(200, json={"status": "ZERO_RESULTS", "results": []})
    )
    reviews = await google_client.get_reviews("存在しない店", "東京都")
    assert reviews == []


@respx.mock
async def test_get_reviews_uses_reviews_field_only(google_client):
    respx.get(f"{PLACES_BASE}/textsearch/json").mock(
        return_value=httpx.Response(200, json=_TEXTSEARCH_OK)
    )
    detail_route = respx.get(f"{PLACES_BASE}/details/json").mock(
        return_value=httpx.Response(200, json=_REVIEWS_OK)
    )
    await google_client.get_reviews("テスト店", "東京都新宿区")
    assert "fields=reviews" in str(detail_route.calls.last.request.url)


# --- enrich_shops ---

async def test_enrich_shops_adds_rating_and_opening_hours():
    mock_client = AsyncMock()
    mock_client.get_place_data.return_value = {
        "rating": 4.5,
        "opening_hours": {
            "open_now": True,
            "weekday_text": ["月曜日: 11:00～23:00"],
        },
    }
    shops = [{"name": "テスト店", "address": "東京都新宿区"}]
    result = await enrich_shops(shops, mock_client)
    gp = result[0]["google_place"]
    assert gp["rating"] == 4.5
    assert gp["current_opening_hours"]["open_now"] is True
    assert gp["current_opening_hours"]["weekday_text"] == ["月曜日: 11:00～23:00"]


async def test_enrich_shops_no_reviews_in_result():
    mock_client = AsyncMock()
    mock_client.get_place_data.return_value = {
        "rating": 4.0,
        "opening_hours": {"open_now": False, "weekday_text": []},
    }
    shops = [{"name": "テスト店", "address": "東京都"}]
    result = await enrich_shops(shops, mock_client)
    assert "reviews" not in result[0]["google_place"]


async def test_enrich_shops_skips_on_failure():
    mock_client = AsyncMock()
    mock_client.get_place_data.side_effect = Exception("API error")
    shops = [{"name": "テスト店", "address": "東京都新宿区"}]
    result = await enrich_shops(shops, mock_client)
    assert "google_place" not in result[0]


async def test_enrich_shops_empty_details():
    mock_client = AsyncMock()
    mock_client.get_place_data.return_value = {}
    shops = [{"name": "テスト店", "address": "東京都"}]
    result = await enrich_shops(shops, mock_client)
    assert "google_place" not in result[0]
