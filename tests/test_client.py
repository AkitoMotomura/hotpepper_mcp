import pytest
import respx
import httpx
from app.client import HotpepperClient

BASE = "http://webservice.recruit.co.jp/hotpepper"

SHOP_FIXTURE = {
    "id": "J000000000",
    "name": "テスト居酒屋",
    "address": "東京都渋谷区",
    "lat": 35.6580,
    "lng": 139.7016,
}


@respx.mock
async def test_get_success(client: HotpepperClient):
    respx.get(f"{BASE}/gourmet/v1/").mock(
        return_value=httpx.Response(200, json={
            "results": {
                "api_version": "1.20",
                "results_available": 1,
                "results_returned": "1",
                "results_start": 1,
                "shop": [SHOP_FIXTURE],
            }
        })
    )
    result = await client.get("/gourmet/v1/", {"keyword": "テスト"})
    assert result["results_available"] == 1
    assert result["shop"][0]["name"] == "テスト居酒屋"


@respx.mock
async def test_get_appends_key_and_format(client: HotpepperClient):
    route = respx.get(f"{BASE}/gourmet/v1/").mock(
        return_value=httpx.Response(200, json={
            "results": {
                "api_version": "1.20",
                "results_available": 0,
                "results_returned": "0",
                "results_start": 1,
                "shop": [],
            }
        })
    )
    await client.get("/gourmet/v1/", {"keyword": "テスト"})
    request = route.calls.last.request
    assert "key=test_key" in str(request.url)
    assert "format=json" in str(request.url)


@respx.mock
async def test_get_filters_none_params(client: HotpepperClient):
    route = respx.get(f"{BASE}/gourmet/v1/").mock(
        return_value=httpx.Response(200, json={
            "results": {
                "api_version": "1.20",
                "results_available": 0,
                "results_returned": "0",
                "results_start": 1,
                "shop": [],
            }
        })
    )
    await client.get("/gourmet/v1/", {"keyword": "テスト", "genre": None})
    request = route.calls.last.request
    assert "genre" not in str(request.url)


@respx.mock
async def test_get_raises_on_api_error(client: HotpepperClient):
    respx.get(f"{BASE}/gourmet/v1/").mock(
        return_value=httpx.Response(200, json={
            "results": {
                "api_version": "1.00",
                "error": [{"message": "keyは必須パラメーターです", "code": 3000}],
            }
        })
    )
    with pytest.raises(RuntimeError, match="HotPepper API error \\[3000\\]"):
        await client.get("/gourmet/v1/", {})


@respx.mock
async def test_get_raises_on_http_error(client: HotpepperClient):
    respx.get(f"{BASE}/gourmet/v1/").mock(
        return_value=httpx.Response(500)
    )
    with pytest.raises(httpx.HTTPStatusError):
        await client.get("/gourmet/v1/", {"keyword": "テスト"})
