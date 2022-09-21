## General Triggers
compose_up:
	docker-compose up -d --build

compose_down:
	docker-compose down

compose_prod_up:
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d --build

compose_prod_down:
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml down