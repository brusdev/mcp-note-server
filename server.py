from pathlib import Path
from mcp.server import MCPServer

NOTES_DIR = Path(__file__).parent / ".notes"
NOTES_DIR.mkdir(exist_ok=True)

mcp = MCPServer("notes")      # our server is born

@mcp.tool()
def add_note(title: str, content: str) -> str:
    """Add a note to my notebook."""
    (NOTES_DIR / f"{title}.txt").write_text(content)
    return f"Saved note '{title}'"

@mcp.resource("notes://{title}")
def read_note(title: str) -> str:
    """Read a note by title."""
    return (NOTES_DIR / f"{title}.txt").read_text()