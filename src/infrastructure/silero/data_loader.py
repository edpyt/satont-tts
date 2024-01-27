from functools import lru_cache
from pathlib import Path

import yaml


@lru_cache
def load_yaml_data(curr_dir: Path) -> dict:
    with open(curr_dir.parent / "silero-pretrained.yml") as f:
        return yaml.safe_load(f)
