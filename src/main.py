from typing import Any, AsyncGenerator

from fastapi import FastAPI

from src.infrastructure.di.main import setup_di
from src.infrastructure.silero.utils import fetch_list_silero_models
from src.presentation.controllers.main import setup_controllers


async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    models: list[Any] = await fetch_list_silero_models()
    setup_di(app, models)
    setup_controllers(app)
    yield


def run_api() -> FastAPI:
    app = FastAPI(title="Silero TTS", version="1.0.0", lifespan=lifespan)
    return app
