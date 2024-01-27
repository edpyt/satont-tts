from dataclasses import dataclass
from typing import Literal


@dataclass
class LangSpeakerTextRequestBody:
    lang: Literal['ru', 'end']
    speaker: str
    text: str
