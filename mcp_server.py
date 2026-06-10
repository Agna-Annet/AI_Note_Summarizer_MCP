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

@mcp.tool()
def count_words(filepath: str)-> int:
    with open(filepath,'r',encoding="utf-8") as file:
        word_count=len(file.read().split())
    return word_count

@mcp.tool()
def extract_headings(filepath: str)-> list:
    with open(filepath,'r', encoding='utf-8') as file:
        headings=[]

        lines=file.read().split("\n")
        for line in lines:
            if line.startswith("#"):
                headings.append(line.strip())

    return headings

#Start MCP server
if __name__=="__main__":
    mcp.run()
