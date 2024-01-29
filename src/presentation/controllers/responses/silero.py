from dataclasses import dataclass

from src.presentation.controllers.responses.base import ErrorResponse, OkResponse


@dataclass(frozen=True)
class SileroSaveWavStatusOk(OkResponse):
    result: str = "Saved .wav file"


@dataclass(frozen=True)
class SileroSaveWavStatusError(ErrorResponse):
    message: str = "Error"


@dataclass(frozen=True)
class SileroDataResponse(OkResponse):
    ...
