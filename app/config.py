"""Settings loaded from environment variables (via the .env file).

Every other module gets its configuration from load_settings(),
so there is exactly one place that reads the environment.
"""

import os
from dataclasses import dataclass

from dotenv import load_dotenv

DEFAULT_MODEL = "claude-haiku-5-5"


@dataclass(frozen=True)
class Settings:
    anthropic_api_key: str
    model: str


def load_settings() -> Settings:
    """Read settings from .env / the environment and fail early if the API key is missing."""
    load_dotenv()

    api_key = os.getenv("ANTHROPIC_API_KEY", "").strip()
    if not api_key:
        raise RuntimeError(
            "ANTHROPIC_API_KEY is not set. Copy .env.example to .env and add your key."
        )

    model = os.getenv("CLAUDE_MODEL", "").strip()
    if not model:
        model = DEFAULT_MODEL

    return Settings(anthropic_api_key=api_key, model=model)
