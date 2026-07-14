from pathlib import Path

import pytest
from pydantic import ValidationError

from sentinel.config.loader import load_config

VALID_CONFIG = """
project:
  name: sentinel-risk-scoring
  random_seed: 42

data:
  input_path: data/raw/telemetry.csv
  artifacts_dir: artifacts
  target: failure_within_24h

training:
  test_size: 0.2
  decision_threshold: 0.5

logging:
  level: INFO
"""


def write_config(tmp_path: Path, content: str = VALID_CONFIG) -> Path:
    """
    Создаёт временный YAML файл.
    """
    config_file = tmp_path / "config.yaml"
    config_file.write_text(content, encoding="utf-8")
    return config_file


def test_load_valid_config(tmp_path: Path):
    """
    Проверяем успешную загрузку корректного YAML.
    """

    config_path = write_config(tmp_path)

    config = load_config(config_path)

    assert config.project.name == "sentinel-risk-scoring"
    assert config.project.random_seed == 42

    assert config.training.test_size == 0.2
    assert config.training.decision_threshold == 0.5

    assert config.data.input_path == Path("data/raw/telemetry.csv")

    assert config.data.artifacts_dir == Path("artifacts")


def test_missing_config_file():
    """
    Проверяем отсутствие файла.
    """

    with pytest.raises(FileNotFoundError):
        load_config(Path("does_not_exist.yaml"))


def test_invalid_training_value(tmp_path: Path):
    """
    test_size больше 1 запрещён.
    """

    invalid_yaml = VALID_CONFIG.replace(
        "test_size: 0.2",
        "test_size: 2.0",
    )

    config_path = write_config(
        tmp_path,
        invalid_yaml,
    )

    with pytest.raises(ValidationError):
        load_config(config_path)


def test_unknown_field(tmp_path: Path):
    """
    Проверяем, что лишние поля запрещены.
    """

    invalid_yaml = VALID_CONFIG.replace(
        "decision_threshold: 0.5",
        "decision_threshhold: 0.5",
    )

    config_path = write_config(
        tmp_path,
        invalid_yaml,
    )

    with pytest.raises(ValidationError):
        load_config(config_path)
