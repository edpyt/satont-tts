from fastapi import FastAPI

from src.infrastructure.di.main import setup_di
from src.presentation.controllers.main import setup_controllers


async def run_api() -> FastAPI:
    app = FastAPI(title="Silero tts", version="1.0.0")
    setup_di(app)
    setup_controllers(app)
    return app
