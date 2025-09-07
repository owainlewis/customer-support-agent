setup:
	@test -d .venv || uv venv
	uv sync --dev
	@echo "Setup complete!"

test:
	uv run pytest

serve:
	uv run uvicorn src.main:app --reload
