[![Verified on MseeP](https://mseep.ai/badge.svg)](https://mseep.ai/app/c99d672f-d0b1-4e89-b834-9b6f313916a9)

# BinoculoMCP

This project is a **Message Control Protocol (MCP) Server** designed to interact with the [Binoculo tool](https://github.com/girorme/binoculo). The goal of this project is to facilitate banner-grabbing operations by sending requests to Binoculo and processing its responses.

<p align="center">
  <a href="https://mseep.ai/app/girorme-binoculo-mcp">
   <img align="center" src="https://mseep.net/pr/girorme-binoculo-mcp-badge.png"/>
  </a>
</p>

## Features

- **Banner Grabbing**: Ask Binoculo to perform operations like "grab all the Apache servers in the 192.168.0.1/24 range."
- **Customizable Queries**: Define specific targets and filters for your banner-grabbing tasks.

## Prerequisites
- Python3
- uv
- Docker (to run binoculo server)
- MCP (sdk)

## Usage
https://github.com/user-attachments/assets/88024174-7cac-496b-a667-56e618890d02

## Installation

### Run binoculo server
```
$ git clone git@github.com:girorme/binoculo.git
$ ./binoculo --server
Starting API server on port 4000
```

### Claude desktop
```
R:\repositorios\binoculo-mcp> uv run mcp install bridge_mcp_binoculo.py
```

> Once the mcp server is istalled via claude, copilot can detect it too

### Mcp config
```json
{
  "mcpServers": {
    "binoculo-mcp": {
      "command": "uv",
      "args": [
        "run",
        "--with",
        "mcp[cli]",
        "--with",
        "requests",
        "mcp",
        "run",
        "R:\\path-to\\binoculo-mcp\\bridge_mcp_binoculo.py"
      ]
    }
  }
}
```

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests to improve this project.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- [Binoculo](https://github.com/girorme/binoculo) for providing the core functionality for banner grabbing.
