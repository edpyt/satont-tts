from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class Response:
    ...


@dataclass(frozen=True)
class StatusResultResponse(Response):
    status: int
    result: Any


@dataclass(frozen=True)
class ClientErrorResponse(StatusResultResponse):
    status: int = 404
    result: str | None = None # error message


@dataclass(frozen=True)
class OkResponse(StatusResultResponse):
    status: int = 200
    result: Any = None
