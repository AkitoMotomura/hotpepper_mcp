import json
from mcp.server.fastmcp import FastMCP
from app.client import HotpepperClient
from app.googleplace.client import GooglePlaceClient
from app.googleplace.enricher import enrich_shops


def register_shop_tools(mcp: FastMCP, client: HotpepperClient, google_client: GooglePlaceClient | None = None) -> None:
    @mcp.tool()
    async def search_shops(
        keyword: str | None = None,
        tel: str | None = None,
        count: int = 10,
        start: int = 1,
    ) -> str:
        """店名・読みがな・住所またはキーワードでHotPepperの店舗を検索する。

        keyword または tel のどちらか一方が必須。
        ヒット件数が30件を超えるとエラーになるため、条件を絞り込んで使用すること。
        tel は半角数字・ハイフンなしで指定（例: 0355500000）。
        Google Places API が設定されている場合、各店舗に rating/current_opening_hours を付加する。
        口コミを取得したい場合は get_restaurant_reviews を使うこと。
        """
        results = await client.get("/shop/v1/", {
            "keyword": keyword,
            "tel": tel,
            "count": count,
            "start": start,
        })
        if google_client and results.get("shop"):
            results["shop"] = await enrich_shops(results["shop"], google_client)
        return json.dumps(results, ensure_ascii=False)
