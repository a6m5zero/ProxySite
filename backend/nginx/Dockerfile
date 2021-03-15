# build environment
FROM node:15.9.0-alpine as build
WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH
COPY ./frontend/client/package.json /app/package.json
RUN npm install --force
COPY ./frontend/client /app
RUN npm run build

FROM nginx:1.19.0-alpine
COPY --from=build /app/dist /usr/share/nginx/html
RUN rm /etc/nginx/conf.d/default.conf
COPY ./backend/nginx/nginx.conf /etc/nginx/conf.d
