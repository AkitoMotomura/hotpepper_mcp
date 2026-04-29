import os
import httpx
from typing import Any

PLACES_BASE_URL = "https://maps.googleapis.com/maps/api/place"

_DETAIL_FIELDS = "rating,opening_hours"
_REVIEW_FIELDS = "reviews"


class GooglePlaceClient:
    def __init__(self, api_key: str | None = None):
        self.api_key = api_key or os.environ["GOOGLE_PLACES_API_KEY"]
        self._client = httpx.AsyncClient(base_url=PLACES_BASE_URL, timeout=10.0)

    async def get_place_data(self, name: str, address: str) -> dict[str, Any]:
        resp = await self._client.get("/textsearch/json", params={
            "query": f"{name} {address}",
            "key": self.api_key,
            "language": "ja",
        })
        resp.raise_for_status()
        search = resp.json()
        if search.get("status") != "OK" or not search.get("results"):
            return {}
        place_id = search["results"][0]["place_id"]

        resp = await self._client.get("/details/json", params={
            "place_id": place_id,
            "fields": _DETAIL_FIELDS,
            "key": self.api_key,
            "language": "ja",
        })
        resp.raise_for_status()
        detail = resp.json()
        if detail.get("status") != "OK":
            return {}

        return detail.get("result", {})

    async def get_reviews(self, name: str, address: str) -> list[dict]:
        resp = await self._client.get("/textsearch/json", params={
            "query": f"{name} {address}",
            "key": self.api_key,
            "language": "ja",
        })
        resp.raise_for_status()
        search = resp.json()
        if search.get("status") != "OK" or not search.get("results"):
            return []
        place_id = search["results"][0]["place_id"]

        resp = await self._client.get("/details/json", params={
            "place_id": place_id,
            "fields": _REVIEW_FIELDS,
            "key": self.api_key,
            "language": "ja",
        })
        resp.raise_for_status()
        detail = resp.json()
        if detail.get("status") != "OK":
            return []
        return detail.get("result", {}).get("reviews", [])

    async def aclose(self):
        await self._client.aclose()
