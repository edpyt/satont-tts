from fastapi import FastAPI

from src.infrastructure.silero.utils import SileroService
from src.infrastructure.di.silero import silero_usecase


def setup_di(app: FastAPI) -> None:
    app.dependency_overrides[SileroService] = silero_usecase
