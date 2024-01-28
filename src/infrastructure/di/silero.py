from typing import Annotated
from fastapi import Depends

from src.infrastructure.silero.service import (
    SileroGetAvailableLangs,
    SileroSaveTTS,
    SileroService,
)
from src.presentation.config import Config


def silero_usecase(config: Annotated[Config, Depends(Config)]) -> SileroService:
    available_langs = SileroGetAvailableLangs(curr_dir=config.current_directory)
    save_tts = SileroSaveTTS(curr_dir=config.current_directory)
  
    return SileroService(available_langs=available_langs, save_tts=save_tts)
