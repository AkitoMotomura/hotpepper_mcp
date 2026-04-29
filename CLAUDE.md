## Overview

HotPepper Gourmet API を MCP (Model Context Protocol) サーバーとして公開するプロジェクト。
FastAPI で MCP サーバーを実装し、Docker コンテナで動作させる。
`GOOGLE_PLACES_API_KEY` が設定されている場合、HotPepper の検索結果に Google Places の
rating・reviews・current_opening_hours を自動付加する。

## Commands

| Command | Description |
|---------|-------------|
| `docker compose up --build` | MCPサーバーをビルドして起動 |
| `docker compose down` | コンテナを停止・削除 |
| `docker compose logs -f` | ログをリアルタイム表示 |
| `docker compose --profile test run --rm test` | テストをコンテナ内で実行 |
| `docker compose --profile test run --rm test pytest -v` | テストを詳細表示で実行 |

## Architecture

```
.
├── app/
│   ├── main.py          # FastAPI エントリーポイント / MCP サーバー定義
│   ├── client.py        # HotPepper API クライアント
│   ├── models.py        # レスポンス・リクエストの Pydantic モデル
│   ├── googleplace/     # Google Places API 連携
│   │   ├── client.py    # Google Places HTTP クライアント（Text Search + Place Details）
│   │   └── enricher.py  # HotPepper 結果を Google 情報で enrich する関数
│   └── tools/           # MCP tool 実装（エンドポイントごと）
├── tests/
│   ├── conftest.py      # pytest fixtures
│   └── test_*.py        # 各ツールのテスト
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
└── hotpeper_api.md      # HotPepper API リファレンス（日本語）
```

## Key Files

- `app/main.py` — FastAPI アプリ + MCP サーバーのエントリーポイント
- `app/client.py` — HotPepper API への HTTP クライアント（`httpx` 使用）
- `app/googleplace/client.py` — Google Places API クライアント
- `app/googleplace/enricher.py` — `enrich_shops(shops, google_client)` で各店舗を enrich
- `hotpeper_api.md` — HotPepper API 全エンドポイントのリファレンス

## Environment

- `HOTPEPPER_API_KEY` — HotPepper API キー（必須）
- `GOOGLE_PLACES_API_KEY` — Google Places API キー（任意。未設定時は enrich をスキップ）

## Google Places Enrichment

`GOOGLE_PLACES_API_KEY` が設定されている場合、`search_restaurants` / `search_shops` の
各店舗に `google_place` フィールドが追加される。

```json
"google_place": {
  "rating": 4.2,
  "user_ratings_total": 312,
  "reviews": [
    { "author_name": "...", "rating": 5, "text": "...", "relative_time_description": "1か月前" }
  ],
  "current_opening_hours": {
    "open_now": true,
    "weekday_text": ["月曜日: 11:00～23:00", ...]
  }
}
```

フロー:
1. HotPepper で店舗リストを取得
2. 各店舗の `name` + `address` で Google Places Text Search → `place_id` を取得
3. Place Details で `rating`, `user_ratings_total`, `reviews`, `opening_hours` を取得
4. 失敗した店舗は `google_place` なしでそのまま返す（エラーで全体を止めない）

## Testing

- テストはすべて Docker 内で実行する（ローカル環境を汚さない）
- `docker compose --profile test run --rm test` で実行
- HotPepper API 呼び出しは `respx` でモック化する（実際の API は叩かない）
- Google Places API 呼び出しも `respx` でモック化する

## Gotchas

- HotPepper API はエラーでも常に HTTP 200 を返す。レスポンスの `<error>` 要素でエラー判定すること
- デフォルトレスポンス形式は XML。`format=json` を常に付与して JSON で受け取る
- `gourmet/v1/` は `key` に加えて最低1つの検索条件パラメータが必須
- 位置検索（`lat`+`lng`）を使うと `order` パラメータ指定に関わらず距離順に強制ソートされる
- Google Places Text Search は店名+住所でマッチするが、同名店舗が複数ある場合は先頭候補を使用する
- Google Places API は店舗が存在しない・情報がない場合 `status: ZERO_RESULTS` を返す（エラーではない）
