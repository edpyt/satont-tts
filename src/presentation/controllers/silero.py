from src.presentation.controllers.requests.silero import (
    LangSpeakerTextRequestBody
)


async def save_speech_to_disk(
    request_body: LangSpeakerTextRequestBody
) -> dict[str, str]:
    return {'status': 'saved'}
