from dataclasses import dataclass

from src.presentation.controllers.responses.base import OkResponse


@dataclass(frozen=True)
class SileroSaveWavStatusOk(OkResponse):
    result: str = "Saved .wav file"


@dataclass(frozen=True)
class SileroDataResponse(OkResponse):
    result: dict
