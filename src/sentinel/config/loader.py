from pathlib import Path

import yaml

from sentinel.config.models import ApplicationConfig


def load_config(path: Path) -> ApplicationConfig:

    if not path.exists():
        raise FileNotFoundError(path)

    if not path.is_file():
        raise ValueError(f"Path is not a file: {path}")

    with path.open("r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    if not isinstance(data, dict):
        raise ValueError("YAML root must be a mapping")

    return ApplicationConfig.model_validate(data)
