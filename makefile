# Makefile (en la raíz del proyecto)

build:
	docker compose build

frontend:
	cd frontend && npm install && npm run build

up:
	docker compose up -d

rebuild: frontend build up

logs:
	docker compose logs -f

restart:
	docker compose down && docker compose up -d

reset-chroma:
	rm -rf chroma/

# Probar si Chroma guarda correctamente
test-chroma:
	python3 test_vector_store.py

migrate:
	docker compose exec django python manage.py migrate
