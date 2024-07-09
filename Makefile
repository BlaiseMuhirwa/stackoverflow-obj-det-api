
generate-api:
	openapi-generator generate \
		-i src/spec/api.yaml \
		-g python \
		-o src/api

install:
	poetry install --no-root 

migrate:
	cd stackoverflow_api && poetry run python manage.py migrate

start-server:
	cd stackoverflow_api && poetry run python manage.py runserver