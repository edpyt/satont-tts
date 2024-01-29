from dataclasses import dataclass
from typing import Literal


@dataclass(frozen=True)
class TTSSaveResultDTO:
    text: str
    speaker: str
    lang: str
    rate: int


@dataclass
class TTSTextDTO:
    text: str


@dataclass
class TTSSaveWavDTO:
    speaker: str
    lang: Literal["ru", "en"]
    rate: Literal["8000", "24000", "48000"]
