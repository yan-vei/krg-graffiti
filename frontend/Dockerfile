# syntax=docker/dockerfile:1.4

FROM node:16-buster-slim as build

WORKDIR /frontend

ENV PATH /app/node_modules/.bin:$PATH

RUN npm install -g @angular/cli

COPY package.json /frontend/package.json
RUN npm i

COPY . /frontend

RUN ng build --configuration production --output-path=dist

FROM nginx:1.14.2

COPY --from=build /frontend/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]

