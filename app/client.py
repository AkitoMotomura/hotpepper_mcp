import os
import httpx
from typing import Any

BASE_URL = "http://webservice.recruit.co.jp/hotpepper"


class HotpepperClient:
    def __init__(self, api_key: str | None = None):
        self.api_key = api_key or os.environ["HOTPEPPER_API_KEY"]
        self._client = httpx.AsyncClient(base_url=BASE_URL, timeout=30.0)

    async def get(self, path: str, params: dict[str, Any]) -> dict:
        clean = {k: v for k, v in params.items() if v is not None}
        clean["key"] = self.api_key
        clean["format"] = "json"
        response = await self._client.get(path, params=clean)
        response.raise_for_status()
        data = response.json()
        results = data["results"]
        if "error" in results:
            error = results["error"][0]
            raise RuntimeError(f"HotPepper API error [{error['code']}]: {error['message']}")
        return results

    async def aclose(self):
        await self._client.aclose()
