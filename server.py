from fastmcp import FastMCP

mcp = FastMCP("Ping MCP Server")


@mcp.tool
def ping() -> str:
    """Check whether the MCP server is available."""
    return "pong"


if __name__ == "__main__":
    mcp.run()