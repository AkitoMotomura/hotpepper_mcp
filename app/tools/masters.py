import json
from mcp.server.fastmcp import FastMCP
from app.client import HotpepperClient


def register_master_tools(mcp: FastMCP, client: HotpepperClient) -> None:
    @mcp.tool()
    async def get_large_areas(keyword: str | None = None) -> str:
        """HotPepperの大エリアマスタを取得する。

        レストラン検索（search_restaurants）で使う large_area コード一覧を返す。
        keyword で大エリア名を部分一致検索できる（例: '東京', '大阪'）。
        """
        results = await client.get("/large_area/v1/", {"keyword": keyword})
        return json.dumps(results, ensure_ascii=False)

    @mcp.tool()
    async def get_middle_areas(
        keyword: str | None = None,
        large_area: str | None = None,
    ) -> str:
        """HotPepperの中エリアマスタを取得する。

        large_area コードで絞り込み可能。keyword で中エリア名を部分一致検索できる。
        """
        results = await client.get("/middle_area/v1/", {
            "keyword": keyword,
            "large_area": large_area,
        })
        return json.dumps(results, ensure_ascii=False)

    @mcp.tool()
    async def get_small_areas(
        keyword: str | None = None,
        middle_area: str | None = None,
    ) -> str:
        """HotPepperの小エリアマスタを取得する。

        middle_area コードで絞り込み可能。keyword で小エリア名を部分一致検索できる。
        """
        results = await client.get("/small_area/v1/", {
            "keyword": keyword,
            "middle_area": middle_area,
        })
        return json.dumps(results, ensure_ascii=False)

    @mcp.tool()
    async def get_genres(keyword: str | None = None) -> str:
        """HotPepperのジャンルマスタを取得する。

        レストラン検索（search_restaurants）で使う genre コード一覧を返す。
        keyword でジャンル名を部分一致検索できる（例: '居酒屋', 'イタリアン'）。
        """
        results = await client.get("/genre/v1/", {"keyword": keyword})
        return json.dumps(results, ensure_ascii=False)

    @mcp.tool()
    async def get_budgets() -> str:
        """HotPepperのディナー予算マスタを取得する。

        レストラン検索（search_restaurants）で使う budget コード一覧を返す。
        """
        results = await client.get("/budget/v1/", {})
        return json.dumps(results, ensure_ascii=False)
