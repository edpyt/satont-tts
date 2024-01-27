from pathlib import Path
from typing import Any, Protocol

from src.infrastructure.silero.data_loader import load_yaml_data


class SileroMeth(Protocol):
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return super().__call__(*args, **kwds)


class SileroGetAvailableLangs(SileroMeth):
    def __init__(self, curr_dir: Path) -> None:
        self._curr_dir = curr_dir

    def __call__(self) -> dict:
        return load_yaml_data(self._curr_dir)


class SileroSaveTTS(SileroMeth):
    async def __call__(self, silero_data: dict) -> Any:
        ...


class SileroService:
    """Silero TTS UseCase object."""

    def __init__(
        self, available_langs: SileroGetAvailableLangs, save_tts: SileroSaveTTS,
    ) -> None:
        self._available_langs = available_langs
        self._save_tts = save_tts

    async def all_available_langs(self) -> dict:
        return self._available_langs()

    async def save_tts(self, lang: str, speaker: str, text: str) -> None:
        data: dict = self._available_langs()
        await self._save_tts(silero_data=data)
