# syntax=docker/dockerfile:1.4

FROM node:16-buster-slim as builder

RUN mkdir /frontend
WORKDIR /frontend

RUN npm install -g @angular/cli@15

COPY package.json package-lock.json ./
RUN npm i --force

COPY . .

EXPOSE 4200

CMD ["ng", "serve", "--host", "0.0.0.0"]
