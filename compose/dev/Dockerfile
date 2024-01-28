FROM python:3.11-slim-bullseye

WORKDIR /code/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./poetry.lock ./pyproject.toml /code/

RUN python -m pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --with api --without task,tts

COPY ./src /code/src
