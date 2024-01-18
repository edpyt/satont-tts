import yaml


def get_tts_yml_data() -> dict:
    with open('silero-pretrained.yml') as f:
        return yaml.safe_load(f)['tts_models']
