# Minimal FastMCP Ping Server

A minimal Python MCP server built with [FastMCP](https://gofastmcp.com/) and managed with [uv](https://docs.astral.sh/uv/). It exposes one tool:

- `ping`: returns `pong`

## Requirements

- Python 3.12 or newer
- uv

## Run

```console
uv sync
uv run fastmcp run server.py:mcp
```

The server uses the stdio transport by default. You can also run it directly:

```console
uv run python server.py
```

## Test

```console
uv run pytest
```

VS Code users can start and debug the server from the MCP servers view using the configuration in `.vscode/mcp.json`.