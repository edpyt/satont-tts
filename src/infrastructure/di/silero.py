import asyncio
from concurrent.futures import ProcessPoolExecutor
import os
from typing import Annotated, Any, Generator

import torch
from fastapi import Depends
from omegaconf import OmegaConf

from src.infrastructure.silero.service import (
    SileroGetAvailableData,
    SileroSaveTTS,
    SileroService,
)
from src.presentation.config import Config


async def silero_models() -> list[Any]:
    res_models = []

    torch.hub.download_url_to_file(
        "https://raw.githubusercontent.com/snakers4/silero-models/master/models.yml",
        "latest_silero_models.yml",
        progress=False,
    )
    models = OmegaConf.load("latest_silero_models.yml")
    loop = asyncio.get_running_loop()

    print('Start parsing Silero TTS Models')
    with ProcessPoolExecutor() as pr_exec:
        for language in models.tts_models.keys():
            for model_id in models.tts_models.get(language).keys():
                if "v4" in model_id:
                    local_file = f"models/{model_id}.pt"
                    if not os.path.isfile(local_file):
                        package_file = (
                            models.tts_models[language][model_id]
                            .latest
                            .package
                        )

                        loop.run_in_executor(
                            pr_exec,
                            torch.hub.download_url_to_file,
                            package_file,
                            local_file,
                        )

                    model = torch.package.PackageImporter(
                        local_file
                    ).load_pickle("tts_models", "model")
                    model.to(torch.device("cpu"))
                    torch.set_num_threads(4)

                    res_models.append(model)
    print('End parsing Silero TTS Models')
    return res_models


def silero_usecase(
    config: Annotated[Config, Depends(Config)],
    silero_models: Annotated[list[Any], Depends(silero_models)],
) -> Generator[SileroService, None, None]:
    available_data = SileroGetAvailableData(
        curr_dir=config.current_directory, models=silero_models
    )
    save_tts = SileroSaveTTS(curr_dir=config.current_directory)

    return SileroService(available_data=available_data, save_tts=save_tts)
