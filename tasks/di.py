from pathlib import Path

from kink import di


def setup_di() -> str:
    curr_dir = Path(__file__).parent
    di["curr_dir"] = curr_dir
