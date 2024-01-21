from pathlib import Path
import yaml


def get_tts_yml_data() -> dict:
    curr_dir = Path(__file__).parent

    with open(curr_dir / 'silero-pretrained.yml') as f:
        return yaml.safe_load(f)
