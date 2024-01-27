from dataclasses import dataclass
from pathlib import Path


@dataclass
class Config:
    current_directory: Path = Path(__file__).parent.parent
