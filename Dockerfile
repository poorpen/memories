FROM python:3.11


ENV POETRY_VERSION=1.7.1

RUN pip install "poetry==$POETRY_VERSION"
RUN apt install make

WORKDIR memories
COPY pyproject.toml /memories/
COPY alembic.ini /memories/
COPY Makefile /memories/

RUN poetry config virtualenvs.create false
RUN poetry install --without dev

COPY ./src /memories/src