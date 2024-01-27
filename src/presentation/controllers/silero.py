from typing import Annotated

from fastapi import Depends

from src.infrastructure.silero.service import SileroService
from src.presentation.controllers.requests.silero import (
    LangSpeakerTextRequestBody,
)
from src.presentation.controllers.responses.silero_data import (
    SileroDataResponse,
)
from src.presentation.providers.stub import Stub


async def save_speech_to_disk(
    request_body: LangSpeakerTextRequestBody,
) -> dict[str, str]:
    return {"status": "saved"}


async def fetch_all_available_langs(
    silero_service: Annotated[SileroService, Depends(Stub(SileroService))],
) -> SileroDataResponse:
    data = await silero_service.all_available_langs()
    return SileroDataResponse(result=data)
