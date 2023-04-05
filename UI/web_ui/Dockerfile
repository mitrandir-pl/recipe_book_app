FROM node:16.14.0-alpine

WORKDIR /UI/web_ui

ENV PATH /UI/web_ui/node_modules/.bin:$PATH

COPY package.json ./
COPY package-lock.json ./
COPY . .

RUN npm install

