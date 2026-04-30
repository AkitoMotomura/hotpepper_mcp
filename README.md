# hotpepper_mcp

[https://zenn.dev/articles/6d6852f6ee43e3/edit](https://zenn.dev/akito1212/articles/6d6852f6ee43e3)

HotPepper Gourmet API を [MCP (Model Context Protocol)](https://modelcontextprotocol.io/) サーバーとして公開するプロジェクト。  
Claude などの AI エージェントからレストラン検索・マスタデータ取得ができる。  
オプションで Google Places API と連携し、評価・口コミ・営業時間を自動付加する。

## API キーの取得

### HotPepper Gourmet API（必須）

1. [リクルート Web サービス](https://webservice.recruit.co.jp/) にアクセス
2. 「新規登録」からアカウントを作成
3. ログイン後、「APIキーの申請」より **ホットペッパーグルメサーチAPI** を申請
4. 発行された API キーを `.env` の `HOTPEPPER_API_KEY` に設定

> 無料で利用可能。1日あたりのリクエスト上限あり（通常 1,000 回/日）。

### Google Places API（任意）

1. [Google Cloud Console](https://console.cloud.google.com/) でプロジェクトを作成
2. 「APIとサービス」→「ライブラリ」から以下を有効化
   - **Places API**
3. 「APIとサービス」→「認証情報」→「認証情報を作成」→「APIキー」
4. 発行された API キーを `.env` の `GOOGLE_PLACES_API_KEY` に設定

> 未設定の場合は Google Places 連携をスキップして動作する（HotPepper 情報のみ返す）。  
> Google Places API は従量課金。無料枠あり（毎月 $200 クレジット）。

## セットアップ

```bash
cp .env.example .env
# .env を編集して API キーを設定

docker compose up --build
```

## アーキテクチャ

```
Claude (MCP Client)
       │  MCP over HTTP (SSE)
       ▼
┌─────────────────────────────────┐
│  MCP Server (FastAPI)           │
│  app/main.py                    │
│                                 │
│  Tools:                         │
│  ・search_restaurants           │
│  ・search_shops                 │
│  ・get_genres / get_budgets     │
│  ・get_*_areas                  │
│  ・get_restaurant_reviews       │
└──────────┬──────────────────────┘
           │
     ┌─────┴──────┐
     ▼            ▼
HotPepper     Google Places API
Gourmet API   (任意 / enrich 用)
```

### データフロー（`search_restaurants` の場合）

```
1. Claude → MCPサーバー: search_restaurants(keyword, lat, lng, ...)
2. MCPサーバー → HotPepper API: /gourmet/v1/?keyword=...&format=json
3. HotPepper API → MCPサーバー: 店舗リスト
4. （GOOGLE_PLACES_API_KEY が設定されている場合）
   MCPサーバー → Google Places Text Search: 店名 + 住所
   Google Places → MCPサーバー: place_id
   MCPサーバー → Google Places Details: place_id
   Google Places → MCPサーバー: rating, reviews, opening_hours
5. MCPサーバー → Claude: 店舗リスト（+ google_place フィールド）
```

### ディレクトリ構成

```
.
├── app/
│   ├── main.py              # FastAPI + MCP サーバー定義
│   ├── client.py            # HotPepper API クライアント
│   ├── models.py            # Pydantic モデル
│   ├── googleplace/
│   │   ├── client.py        # Google Places HTTP クライアント
│   │   └── enricher.py      # HotPepper 結果を Google 情報で enrich
│   └── tools/               # MCP tool 実装
├── tests/
├── Dockerfile
├── docker-compose.yml
└── pyproject.toml
```

## コマンド

| コマンド | 説明 |
|---------|------|
| `docker compose up --build` | MCP サーバーをビルドして起動 |
| `docker compose down` | コンテナを停止・削除 |
| `docker compose logs -f` | ログをリアルタイム表示 |
| `docker compose --profile test run --rm test` | テストを実行 |
