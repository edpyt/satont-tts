from fastapi import FastAPI

from src.infrastructure.di.config import config_obj
from src.infrastructure.di.silero import silero_usecase
from src.infrastructure.silero.service import SileroService
from src.presentation.config import Config
from src.presentation.providers.stub import Stub


def setup_di(app: FastAPI) -> None:
    app.dependency_overrides[Config] = config_obj
    app.dependency_overrides[Stub(SileroService)] = silero_usecase
