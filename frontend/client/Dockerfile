FROM node:15.9.0-alpine

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

COPY package.json /app/package.json
RUN npm install --force

COPY . /app

# start app
CMD npm run serve
# -- host 0.0.0.0