# MCP Note Server

A minimal [Model Context Protocol](https://modelcontextprotocol.io) (MCP) server, written in Python, that gives AI assistants a simple notebook. Notes are stored as plain `.txt` files in a local `.notes/` directory.

> **Demo only.** This project exists to demonstrate how to build and connect a basic MCP server. It is not production-ready: it has no authentication, no input validation, and no error handling. Don't use it to store sensitive information or run it in a shared or exposed environment.

## Features

| Type     | Name              | Description                                 |
|----------|-------------------|---------------------------------------------|
| Tool     | `add_note`        | Save a note. Arguments: `title`, `content`. |
| Resource | `notes://{title}` | Read the content of a note by its title.    |

The server is implemented in [`server.py`](server.py) and talks to clients over stdio.

## Requirements

- Python 3.10+
- The [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) with the CLI extras

## Installation

```bash
git clone https://github.com/brusdev/mcp-note-server.git
cd mcp-note-server
python -m venv .venv
source .venv/bin/activate
pip install "mcp[cli]"
```

Test and inspect the server using the MCP Inspector:

```bash
mcp dev server.py
```

## Using the server with AI apps

This repository doesn't ship any client configuration. In the examples below, replace `/absolute/path/to/mcp-note-server` with the location of your clone. Use absolute paths and point `command` to the `mcp` executable inside your virtual environment, so the app doesn't depend on your shell `PATH`.

### IBM Bob

Bob reads MCP servers from `~/.bob/mcp.json` (global) or `.bob/mcp.json` in a project root (project level). Add the server to either file:

```json
{
  "mcpServers": {
    "notes": {
      "command": "/absolute/path/to/mcp-note-server/.venv/bin/mcp",
      "args": ["run", "/absolute/path/to/mcp-note-server/server.py"]
    }
  }
}
```

1. Save the file.
2. Open the MCP settings in Bob and confirm the `notes` server is enabled.
3. Ask Bob: *"Add a note titled `ideas` with the content `Write a README`"*.

### Claude Desktop

Edit `claude_desktop_config.json` (Settings → Developer → Edit Config):

```json
{
  "mcpServers": {
    "notes": {
      "command": "/absolute/path/to/mcp-note-server/.venv/bin/mcp",
      "args": ["run", "/absolute/path/to/mcp-note-server/server.py"]
    }
  }
}
```

Restart Claude Desktop, then ask Claude to add a note.

### GitHub Copilot in VS Code

Create `.vscode/mcp.json` in your workspace (or run **MCP: Add Server** from the Command Palette):

```json
{
  "servers": {
    "notes": {
      "type": "stdio",
      "command": "/absolute/path/to/mcp-note-server/.venv/bin/mcp",
      "args": ["run", "/absolute/path/to/mcp-note-server/server.py"]
    }
  }
}
```

Switch Copilot Chat to Agent mode and enable the `notes` tools.

## Example prompts

- "Add a note called `shopping` with milk, eggs and bread."
- "Read the note `shopping`."

## Limitations

- Notes are stored in the `.notes/` directory next to `server.py`, which is created on startup and excluded from version control.
- The note title is used as the file name without sanitization, so path separators in a title are not handled safely.
- Reading a note that doesn't exist returns an error.

## License

See [LICENSE](LICENSE).
