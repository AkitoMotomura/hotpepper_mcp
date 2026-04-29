import asyncio
import logging
from typing import Any

from app.googleplace.client import GooglePlaceClient

logger = logging.getLogger(__name__)

_CONCURRENCY = 5


async def _enrich_shop(shop: dict[str, Any], client: GooglePlaceClient, sem: asyncio.Semaphore) -> dict[str, Any]:
    name = shop.get("name", "")
    if not name:
        return shop

    try:
        async with sem:
            details = await client.get_place_data(name, shop.get("address", ""))
    except Exception as e:
        logger.warning("Google Places enrichment failed for %s: %s", name, e)
        return shop

    if not details:
        return shop

    google_data: dict[str, Any] = {
        field: details[field]
        for field in ("rating",)
        if field in details
    }
    if "opening_hours" in details:
        oh = details["opening_hours"]
        google_data["current_opening_hours"] = {
            "open_now": oh.get("open_now"),
            "weekday_text": oh.get("weekday_text", []),
        }

    shop["google_place"] = google_data
    return shop


async def enrich_shops(shops: list[dict[str, Any]], client: GooglePlaceClient) -> list[dict[str, Any]]:
    sem = asyncio.Semaphore(_CONCURRENCY)
    return await asyncio.gather(*[_enrich_shop(shop, client, sem) for shop in shops])
