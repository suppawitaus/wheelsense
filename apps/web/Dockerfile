FROM node:20-alpine

WORKDIR /app
COPY package.json ./
COPY tsconfig.json ./
COPY next.config.mjs ./
COPY src ./src

RUN npm install --silent
EXPOSE 3000
CMD ["npm", "run", "dev", "--", "-p", "3000", "-H", "0.0.0.0"]
