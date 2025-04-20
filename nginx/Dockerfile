# Etapa 1: Construcción de Svelte
FROM node:18-alpine AS builder

WORKDIR /app
COPY ../frontend/package*.json ./
RUN npm install
COPY ../frontend ./
RUN npm run build

# Etapa 2: Servir con Nginx
FROM nginx:alpine

COPY ./nginx/nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /app/dist /usr/share/nginx/html
