from dataclasses import dataclass
from typing import Literal


@dataclass
class TTSSaveWavDTO:
    lang: Literal["ru", "en"]
    speaker: str
    text: str
