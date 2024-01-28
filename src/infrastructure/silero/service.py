# TODO: Add docstrings

import os
from abc import ABCMeta
from pathlib import Path
from typing import Any, Protocol

from torch import device as t_device
from torch.hub import download_url_to_file
from torch.package import PackageImporter

from src.application.silero.dto.save_model import TTSSaveWavDTO
from src.infrastructure.silero.data_loader import load_yaml_data


class SileroModelFile(metaclass=ABCMeta):
    def __init__(self, curr_dir: Path) -> None:
        self._curr_dir = curr_dir


class SileroMeth(Protocol):
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return super().__call__(*args, **kwds)


class SileroGetAvailableLangs(SileroMeth, SileroModelFile):
    def __call__(self) -> dict:
        return load_yaml_data(self._curr_dir)


class SileroSaveTTS(SileroMeth, SileroModelFile):
    async def __call__(self, silero_data: dict, save_wav_dto: TTSSaveWavDTO) -> Any:
        package_data = self._get_package_data(silero_data, save_wav_dto)
        if not package_data:
            return "Error"
        package, rate = package_data
        device = t_device("cpu")
        model = self._get_model(device, package, save_wav_dto.speaker)
        model.save_wav(text=save_wav_dto.text, speaker=save_wav_dto.speaker, sample_rate=rate)

    def _get_package_data(self, silero_data: dict, save_wav_dto: TTSSaveWavDTO) -> tuple[str, int] | None:
        try:
            model_data = silero_data[save_wav_dto.lang][save_wav_dto.speaker]
        except KeyError:
            return 
        package = model_data["latest"].get("package")
        if not package:
            package = model_data["latest"]["jit"]

        sample_rate = model_data["latest"]["sample_rate"]
        if isinstance(sample_rate, list):
            sample_rate = sample_rate[-1]

        return package, sample_rate

    def _get_model(self, device: Any, package: Any, model: str = 'model') -> Any:
        local_model_file = f"{self._curr_dir.parent}/models/{model}.pt"
        if not os.path.isfile(local_model_file):
            download_url_to_file(package, local_model_file)

        package_importer = PackageImporter(local_model_file)
        model = package_importer.load_pickle("tts_models", "model")
        model.to(device)

        return model


class SileroService:
    """Silero TTS UseCase object."""

    def __init__(
        self, available_langs: SileroGetAvailableLangs, save_tts: SileroSaveTTS,
    ) -> None:
        self._available_langs = available_langs
        self._save_tts = save_tts

    async def all_available_langs(self) -> dict:
        return self._available_langs()

    async def save_tts(self, save_wav_dto: TTSSaveWavDTO) -> None:
        data: dict = self._available_langs()
        await self._save_tts(silero_data=data, save_wav_dto=save_wav_dto)
