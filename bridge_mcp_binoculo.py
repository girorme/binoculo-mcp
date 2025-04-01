from mcp.server.fastmcp import FastMCP
import requests
import sys
import socket

binoculo_server_url = "http://localhost:4000"
mcp = FastMCP("binoculo-mcp", dependencies=["requests"])

def post(endpoint: str, data: dict | str) -> str:
    try:
        response = requests.post(f"{binoculo_server_url}/{endpoint}", json=data, timeout=10)
        if response.ok:
            print(response.text, file=sys.stderr)
            return response.text
        else:
            return f"Error {response.status_code}: {response.text.strip()}"
    except Exception as e:
        return f"Request failed: {str(e)}"

@mcp.tool()
def get_banners(host_notation: str, ports: str) -> str:
    """
    Get banners for the given host notation and ports (cidr: 192.168.0.1/24 or range: 192.168.0.1-192.168.0.255)
    If you want to get all the banners for a host range, first use the `get_host_by_name` tool
    """
    return post("start", {"host_notation": host_notation, "ports": ports})

@mcp.tool()
def get_host_by_name(name: str) -> str:
    """
    Get the IP address for the given host name
    """
    return socket.gethostbyname(name)