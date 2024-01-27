from typing import Any, Protocol


class SileroMeth(Protocol):
    ...


class SileroGetAvailableLangs(SileroMeth):
    ...


class SileroSaveTTS(SileroMeth):
    async def __call__(self, *args: Any, **kwds: Any) -> Any:
        return super().__call__(*args, **kwds)


class SileroService:
    """Silero TTS UseCase object"""

    def __init__(
        self, available_langs: SileroMeth, save_tts: SileroMeth
    ) -> None:
        self._available_langs = available_langs
        self._save_tts = save_tts

    async def save_tts(self, lang: str, speaker: str, text: str) -> None:
        
        await self._save_tts()
