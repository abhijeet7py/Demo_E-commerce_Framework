"""Configuration reader for environment-aware test execution."""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, Dict


class ConfigReader:
    """Loads framework configuration from a JSON file."""

    def __init__(self, config_path: str = "config/settings.json") -> None:
        self.config_path = Path(config_path)
        self._config_data = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        with self.config_path.open("r", encoding="utf-8") as file:
            return json.load(file)

    def get_env_config(self) -> Dict[str, Any]:
        requested_env = os.getenv("TEST_ENV")
        active_env = requested_env or self._config_data["default_env"]
        return self._config_data["environments"][active_env]
