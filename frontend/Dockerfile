# syntax=docker/dockerfile:1.4

FROM node:16-buster-slim as builder

WORKDIR /frontend

ENV PATH /app/node_modules/.bin:$PATH

RUN npm install -g @angular/cli

COPY package.json /frontend/package.json
RUN npm i

COPY . /frontend

EXPOSE 3080

CMD ["ng", "serve", "--host", "0.0.0.0", "--port", "3080"]
