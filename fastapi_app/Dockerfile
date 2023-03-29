FROM python:3.10

WORKDIR /fastapi_app

COPY ./poetry.lock /poetry.lock
COPY ./pyproject.toml /pyproject.toml
COPY ./entrypoint.sh /entrypoint.sh
COPY . .

RUN python -m pip install --upgrade pip
RUN pip install poetry
RUN poetry install
