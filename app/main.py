import os
from contextlib import asynccontextmanager
from fastapi import FastAPI
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

from app.client import HotpepperClient
from app.googleplace.client import GooglePlaceClient
from app.tools.gourmet import register_gourmet_tools
from app.tools.shop import register_shop_tools
from app.tools.masters import register_master_tools

load_dotenv()

mcp = FastMCP("hotpepper-gourmet")
_client: HotpepperClient | None = None
_google_client: GooglePlaceClient | None = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    global _client, _google_client
    _client = HotpepperClient()
    if os.environ.get("GOOGLE_PLACES_API_KEY"):
        _google_client = GooglePlaceClient()
    register_gourmet_tools(mcp, _client, _google_client)
    register_shop_tools(mcp, _client, _google_client)
    register_master_tools(mcp, _client)
    yield
    await _client.aclose()
    if _google_client:
        await _google_client.aclose()


app = FastAPI(title="HotPepper MCP Server", version="0.1.0", lifespan=lifespan)


@app.get("/health")
async def health():
    return {"status": "ok"}


app.mount("/", mcp.sse_app())
