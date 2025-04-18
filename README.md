# BinoculoMCP (WIP)

This project is a **Message Control Protocol (MCP) Server** designed to interact with the [Binoculo tool](https://github.com/girorme/binoculo). The goal of this project is to facilitate banner-grabbing operations by sending requests to Binoculo and processing its responses.

## Features

- **Banner Grabbing**: Ask Binoculo to perform operations like "grab all the Apache servers in the 192.168.0.1/24 range."
- **Customizable Queries**: Define specific targets and filters for your banner-grabbing tasks.
- **Work in Progress**: This project is under active development, and new features are being added regularly.

## Prerequisites
- Python3
- uv
- Docker (soon)
- MCP (sdk)
- Run binoculo server

## Usage
https://github.com/user-attachments/assets/88024174-7cac-496b-a667-56e618890d02

## Installation
### Claude desktop
```
R:\repositorios\binoculo-mcp> uv run mcp install bridge_mcp_binoculo.py
```

### Run binoculo server
- TODO

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests to improve this project.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- [Binoculo](https://github.com/girorme/binoculo) for providing the core functionality for banner grabbing.
