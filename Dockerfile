FROM  node:22.21.0-alpine AS build

WORKDIR /app

COPY package*.json .

RUN npm install 

COPY . .

RUN npm run build

FROM  node:22.21.0-alpine

WORKDIR /app

COPY --from=build /app/package*.json  .

RUN npm install --production

COPY --from=build /app/dist ./dist

EXPOSE 3000

CMD [ "node","./dist/index.js" ]