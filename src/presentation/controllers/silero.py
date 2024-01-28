from typing import Annotated, Literal

from fastapi import Depends, Form

from src.infrastructure.silero.service import SileroService
from src.presentation.controllers.requests.silero import (
    LangSpeakerTextRequestBody,
)
from src.presentation.controllers.responses.silero_data import (
    SileroDataResponse,
)
from src.presentation.providers.stub import Stub


async def save_speech_to_disk(
    lang: Annotated[Literal["ru", "en"], Form(title='Language')],
    speaker: Annotated[str, Form(title='Speaker')],
    text: Annotated[str, Form(title='Text')],
) -> dict[str, str]:
    request_body = LangSpeakerTextRequestBody(lang, speaker, text)
    return {"status": "saved"}


async def fetch_all_available_langs(
    silero_service: Annotated[SileroService, Depends(Stub(SileroService))],
) -> SileroDataResponse:
    data = await silero_service.all_available_langs()
    return SileroDataResponse(result=data)
