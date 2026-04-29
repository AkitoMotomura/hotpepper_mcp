import json
from mcp.server.fastmcp import FastMCP
from app.client import HotpepperClient
from app.googleplace.client import GooglePlaceClient
from app.googleplace.enricher import enrich_shops


def register_gourmet_tools(mcp: FastMCP, client: HotpepperClient, google_client: GooglePlaceClient | None = None) -> None:
    @mcp.tool()
    async def search_restaurants(
        keyword: str | None = None,
        large_area: str | None = None,
        middle_area: str | None = None,
        small_area: str | None = None,
        lat: float | None = None,
        lng: float | None = None,
        range: int | None = None,
        genre: str | None = None,
        budget: str | None = None,
        count: int = 10,
        start: int = 1,
        private_room: bool = False,
        free_drink: bool = False,
        free_food: bool = False,
        lunch: bool = False,
        non_smoking: bool = False,
        course: bool = False,
        card: bool = False,
    ) -> str:
        """HotPepperグルメでレストランを検索する。

        エリアコード・キーワード・位置情報などで絞り込み可能。
        keyword, large_area, lat+lng のいずれか最低1つが必要。
        エリアコードは get_large_areas / get_middle_areas / get_small_areas で取得できる。
        ジャンルコードは get_genres、予算コードは get_budgets で取得できる。
        range は 1=300m, 2=500m, 3=1000m(初期値), 4=2000m, 5=3000m。
        Google Places API が設定されている場合、各店舗に rating/current_opening_hours を付加する。
        口コミを取得したい場合は get_restaurant_reviews を使うこと。
        """
        results = await client.get("/gourmet/v1/", {
            "keyword": keyword,
            "large_area": large_area,
            "middle_area": middle_area,
            "small_area": small_area,
            "lat": lat,
            "lng": lng,
            "range": range,
            "genre": genre,
            "budget": budget,
            "count": count,
            "start": start,
            "private_room": 1 if private_room else None,
            "free_drink": 1 if free_drink else None,
            "free_food": 1 if free_food else None,
            "lunch": 1 if lunch else None,
            "non_smoking": 1 if non_smoking else None,
            "course": 1 if course else None,
            "card": 1 if card else None,
        })
        if google_client and results.get("shop"):
            results["shop"] = await enrich_shops(results["shop"], google_client)
        return json.dumps(results, ensure_ascii=False)

    @mcp.tool()
    async def get_restaurant_reviews(name: str, address: str) -> str:
        """指定した店舗のGoogle Places口コミを取得する。

        search_restaurants で得た店舗の name と address をそのまま渡すこと。
        Google Places API が設定されていない場合はエラーを返す。
        """
        if not google_client:
            return json.dumps({"error": "Google Places API が設定されていません"}, ensure_ascii=False)
        reviews = await google_client.get_reviews(name, address)
        result = [
            {field: r.get(field) for field in ("author_name", "rating", "text", "relative_time_description")}
            for r in reviews
        ]
        return json.dumps({"name": name, "reviews": result}, ensure_ascii=False)
