from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class Response:
    ...


@dataclass(frozen=True)
class StatusResponse(Response):
    status: int
    message: Any


@dataclass(frozen=True)
class ErrorResponse(StatusResponse):
    status: int = 400
    message: str | None = None


@dataclass(frozen=True)
class OkResponse(StatusResponse):
    status: int = 200
    message: Any = None
