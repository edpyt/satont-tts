from typing import Annotated, Any, Generator

from fastapi import Depends

from src.infrastructure.silero.service import (
    SileroGetAvailableData,
    SileroSaveTTS,
    SileroService,
)
from src.presentation.config import Config


async def silero_models() -> None:
    ...


def silero_usecase(
    config: Annotated[Config, Depends(Config)],
    silero_models: Annotated[list[Any], Depends(silero_models)],
) -> Generator[SileroService, None, None]:
    available_data = SileroGetAvailableData(
        curr_dir=config.current_directory, models=silero_models
    )
    save_tts = SileroSaveTTS(curr_dir=config.current_directory)

    return SileroService(available_data=available_data, save_tts=save_tts)
