from fastapi import FastAPI

from src.presentation.controllers.silero import (
    fetch_all_available_langs,
    save_speech_to_disk,
)


def setup_controllers(app: FastAPI) -> None:
    app.add_api_route("/speech", save_speech_to_disk)
    app.add_api_route("/silero_data", fetch_all_available_langs)
