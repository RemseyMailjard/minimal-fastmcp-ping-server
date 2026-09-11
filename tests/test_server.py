import asyncio

from fastmcp import Client

from server import mcp


def test_ping_returns_pong() -> None:
    async def call_ping() -> str:
        async with Client(mcp) as client:
            result = await client.call_tool("ping", {})
            return result.data

    assert asyncio.run(call_ping()) == "pong"