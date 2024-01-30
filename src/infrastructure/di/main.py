import logging
from typing import Any

from fastapi import FastAPI

from src.infrastructure.di.config import config_obj
from src.infrastructure.di.log import logger
from src.infrastructure.di.silero import silero_models, silero_usecase
from src.infrastructure.silero.service import SileroService
from src.presentation.config import Config
from src.presentation.providers.stub import Stub


def setup_di(app: FastAPI, s_models: list[Any]) -> None:
    app.dependency_overrides[Config] = config_obj

    app.dependency_overrides[logging.Logger] = logger

    # startup Silero TTS models loading
    app.dependency_overrides[silero_models] = lambda: s_models
    app.dependency_overrides[Stub(SileroService)] = silero_usecase
