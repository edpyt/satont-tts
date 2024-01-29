from dataclasses import asdict
from typing import Annotated

from fastapi import Depends

from src.application.silero.dto.save_model import TTSSaveResultDTO, TTSSaveWavDTO, TTSTextDTO
from src.infrastructure.silero.service import SileroService
from src.presentation.controllers.responses.silero import (
    SileroDataResponse,
    SileroSaveWavStatusOk,
)
from src.presentation.providers.stub import Stub


async def save_speech_to_disk(
    text: TTSTextDTO,
    save_wav_dto: TTSSaveWavDTO = Depends(),
    silero_service: SileroService = Depends(Stub(SileroService)),
) -> SileroSaveWavStatusOk:
    save_wav_dto.rate = int(save_wav_dto.rate)
    tts_save_dto = TTSSaveResultDTO(**asdict(text), **asdict(save_wav_dto))
    return SileroSaveWavStatusOk()


async def fetch_all_available_langs(
    silero_service: Annotated[SileroService, Depends(Stub(SileroService))],
) -> SileroDataResponse:
    data = await silero_service.all_available_langs()
    return SileroDataResponse(result=data)
