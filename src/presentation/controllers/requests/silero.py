from dataclasses import dataclass
from typing import Literal


@dataclass
class LangSpeakerTextRequestBody:
    lang: Literal["ru", "en"]
    speaker: str
    text: str
