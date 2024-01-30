import asyncio
import os
from concurrent.futures import ProcessPoolExecutor
from typing import Any

import torch
from omegaconf import OmegaConf


def fetch_list_silero_models() -> list[Any]:
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
