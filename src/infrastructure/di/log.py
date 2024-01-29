import logging


def logger() -> logging.Logger:
    return logging.getLogger("uvicorn")
