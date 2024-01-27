from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class Response:
    ...


@dataclass(frozen=True)
class OkResponse(Response):
    status: int = 200
    result: Any = None
