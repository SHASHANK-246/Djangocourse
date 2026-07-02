FROM python:3.12-bullseye AS base

ENV PYTHONUNBUFFERED=1

RUN apt update

RUN apt install gettext -y

RUN mkdir /code

WORKDIR /code

RUN pip install poetry

COPY pyproject.toml poetry.lock ./

FROM base AS development

RUN poetry install --no-root

COPY . .

EXPOSE 8000

RUN chmod +x /code/start-django.sh

ENTRYPOINT ["/code/start-django.sh" ]                     

FROM base AS production

RUN poetry install --only main --no-root

COPY . .

EXPOSE 8000

RUN chmod +x /code/start-django.sh

ENTRYPOINT ["/code/start-django.sh" ]  