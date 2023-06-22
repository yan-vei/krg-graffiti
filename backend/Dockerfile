# syntax=docker/dockerfile:1.4

FROM python:3.10.1-slim

ENV DB_CONTAINER_NAME db

COPY . /app
WORKDIR /app

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

RUN pip install -r requirements.txt

WORKDIR /app/src
EXPOSE 5000

CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000" ]