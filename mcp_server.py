"""
MCP SERVER

This server exposes a tool that reads a markdown file and returns its content

"""

from mcp.server.fastmcp import FastMCP

#Create MCP Server
mcp= FastMCP("MarkdownServer")

@mcp.tool() #makes function avaailable to the clients
def read_markdown(filepath: str) -> str:
    """
    Read a markdown file

    Argument: The filepath 

    Returns: The file contents as a string
    """

    with open(filepath,"r",encoding="utf-8") as file:
        content=file.read()
    return content


#Start MCP server
if __name__=="__main__":
    mcp.run()
