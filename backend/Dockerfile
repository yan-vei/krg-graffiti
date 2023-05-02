# syntax=docker/dockerfile:1.4


FROM python:3.10.1-slim

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

WORKDIR /app/src

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]