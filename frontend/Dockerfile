# build step
FROM node:16.13.2-alpine

WORKDIR /usr/app
COPY src/package.json ./
RUN npm install
COPY src ./
# RUN npm run start