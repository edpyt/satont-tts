import asyncio
import os
from concurrent.futures import ProcessPoolExecutor

from kink import inject
from torch import device as t_device
from torch.hub import download_url_to_file
from torch.package import PackageImporter

from yml_data import get_tts_yml_data


@inject
def save_speech_to_file(
    device: t_device,
    package: str,
    rate: int,
    speaker: str,
    text: str,
    curr_dir: str
) -> None:
    """Save speech to wav file"""

    local_file = f'{curr_dir}/model.pt'
    if not os.path.isfile(local_file):
        download_url_to_file(package, local_file)

    package_importer = PackageImporter(local_file)
    model = package_importer.load_pickle('tts_models', 'model')
    print(type(model))
    return

    model.to(device)

    model.save_wav(text=text, speaker=speaker, sample_rate=rate)


async def get_speaker_package_data(
    silero_data: dict, lang: str, speaker: str
) -> tuple[str, int] | None:
    """Get package url and max rate number"""

    try:
        model_data = silero_data[lang][speaker]
    except KeyError:
        print(
            '\033[101m'
            'Data with provided key/value pair lang, speeker not found'
            '\033[0m'
        )
        return None

    package = model_data['latest'].get('package')
    if not package:
        package = model_data['latest']['jit']

    sample_rate = model_data['latest']['sample_rate']

    if isinstance(sample_rate, list):
        sample_rate = sample_rate[0]

    return package, sample_rate


async def asave_tts(lang: str, speaker: str, text: str) -> None:
    """Main event loop"""

    loop = asyncio.get_running_loop()

    silero_data: dict = get_tts_yml_data()
    package_data = await get_speaker_package_data(
        silero_data, lang, speaker
    )

    if not package_data:
        return None
    package, rate = package_data

    device = t_device('cpu')
    with ProcessPoolExecutor() as pr_executor:
        loop.run_in_executor(
            pr_executor,

            save_speech_to_file,
            device,
            package,
            rate,
            speaker,
            text
        )


def main(lang: str, speaker: str, text: str) -> None:
    """
    Function which need to accept lang + speaker + text which will save audio
    file to disk
    """

    asyncio.run(asave_tts(lang, speaker, text))


if __name__ == '__main__':
    main('ru', 'aidar_v2',  'Здаврова')
