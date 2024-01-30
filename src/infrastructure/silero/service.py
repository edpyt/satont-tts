# TODO: Add docstrings

from abc import ABCMeta
from pathlib import Path
from typing import Any, Protocol

from src.application.silero.dto.save_model import TTSSaveResultDTO


class SileroModelFile(metaclass=ABCMeta):
    def __init__(self, curr_dir: Path) -> None:
        self._curr_dir = curr_dir


class SileroMeth(Protocol):
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return super().__call__(*args, **kwds)


class SileroGetAvailableData(SileroMeth, SileroModelFile):
    def __init__(self, curr_dir: Path, models: Any) -> None:
        self._models = models
        super().__init__(curr_dir)

    def __call__(self) -> list:
        return [
            {
                "symbols": str(model.symbols),
                "speakers": model.speakers,
            }
            for model in self._models
        ]


class SileroSaveTTS(SileroMeth, SileroModelFile):
    async def __call__(self, silero_data: dict, save_wav_dto: TTSSaveResultDTO) -> str | None:
        return "Ok"


class SileroService:
    """Silero TTS UseCase object."""

    def __init__(
        self, available_data: SileroGetAvailableData, save_tts: SileroSaveTTS,
    ) -> None:
        self._available_data = available_data
        self._save_tts = save_tts

    async def all_available_data(self) -> list:
        return self._available_data()

    async def save_tts(self, save_wav_dto: TTSSaveResultDTO) -> str | None:
        data: list = self._available_data()
        return await self._save_tts(silero_data=data, save_wav_dto=save_wav_dto)
