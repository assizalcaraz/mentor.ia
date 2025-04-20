build:
	cd frontend && npm install && npm run build

copy:
	docker cp frontend/dist/. mentoria-nginx-1:/usr/share/nginx/html/

deploy: build copy

front-redeploy:
	cd frontend && rm -rf dist .svelte-kit && npm install && npm run build
	docker exec -it mentoria-nginx-1 rm -rf /usr/share/nginx/html/*
	docker cp frontend/dist/. mentoria-nginx-1:/usr/share/nginx/html/

backend:
	docker compose down && docker compose down --build -d
web:
	make deploy && docker compose up -d

force:
	make front-redeploy && make backend