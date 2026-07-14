from pathlib import Path

from pydantic import BaseModel, ConfigDict, Field


class ProjectConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str
    random_seed: int


class DataConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    input_path: Path
    artifacts_dir: Path
    target: str


class TrainingConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    test_size: float = Field(gt=0, lt=1)
    decision_threshold: float = Field(ge=0, le=1)


class LoggingConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    level: str


class ApplicationConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    project: ProjectConfig
    data: DataConfig
    training: TrainingConfig
    logging: LoggingConfig
