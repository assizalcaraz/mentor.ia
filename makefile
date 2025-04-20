build:
	docker compose build

front:
	cd frontend && rm -rf dist .svelte-kit && npm run build

up:
	docker compose up --build -d

rebuild: front build up

logs:
	docker compose logs -f

restart:
	docker compose down && docker compose up -d

ok: rebuild
