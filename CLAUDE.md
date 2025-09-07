# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

- **Setup environment**: `make setup` - Creates virtual environment and installs dependencies
- **Run development server**: `make serve` - Starts FastAPI server on localhost:8000 with hot reload
- **Run tests**: `make test` - Executes pytest test suite

## Architecture Overview

This is a Pydantic AI-powered customer support agent built with FastAPI. The project uses `uv` for Python dependency management and requires Python 3.13+.

### Core Structure
- `src/main.py` - FastAPI application entry point with router mounting
- `src/api/router.py` - API route definitions (currently contains a basic ping endpoint)
- `src/agents/customer_support_agent.py` - Customer support agent implementation (currently empty)

### Key Dependencies
- **FastAPI**: Web framework for API endpoints
- **pydantic-ai**: AI agent framework for building intelligent agents
- **pydantic-settings**: Configuration management

### Development Setup
The project uses `uv` for dependency management. Run `make setup` to create a virtual environment and install all dependencies including development tools like ipykernel for Jupyter notebook support.

### API Structure
- Base API is mounted at `/v1` prefix
- Current endpoints are minimal (ping endpoint for health checks)
- Agent functionality is intended to be built in the `agents/` module