from dataclasses import asdict
from typing import Annotated

from fastapi import Depends
from fastapi.responses import JSONResponse

from src.application.silero.dto.save_model import TTSSaveResultDTO, TTSSaveWavDTO, TTSTextDTO
from src.infrastructure.silero.service import SileroService
from src.presentation.controllers.responses.base import StatusResponse
from src.presentation.controllers.responses.silero import (
    SileroDataResponse,
    SileroSaveWavStatusError,
    SileroSaveWavStatusOk,
)
from src.presentation.providers.stub import Stub


async def save_speech_to_disk(
    text: TTSTextDTO,
    save_wav_dto: TTSSaveWavDTO = Depends(),
    silero_service: SileroService = Depends(Stub(SileroService)),
) -> JSONResponse:
    save_wav_dto.rate = int(save_wav_dto.rate)
    tts_save_dto = TTSSaveResultDTO(**asdict(text), **asdict(save_wav_dto))

    save_status: str | None = await silero_service.save_tts(tts_save_dto)
    response: StatusResponse | None = None
    if save_status is None:
        response = SileroSaveWavStatusError(message="Bad model provided!")
    else:
        response = SileroSaveWavStatusOk()

    return JSONResponse(status_code=response.status, content=response.message)


async def fetch_all_available_langs(
    silero_service: Annotated[SileroService, Depends(Stub(SileroService))],
) -> JSONResponse:
    data = await silero_service.all_available_langs()
    response = SileroDataResponse(message=data)
    return JSONResponse(status_code=response.status, content=response.message)
