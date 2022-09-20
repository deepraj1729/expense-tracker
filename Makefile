## General Triggers
compose_up:
	docker-compose up -d --build

compose_down:
	docker-compose down

compose_prod_up:
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d --build

compose_prod_down:
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml down


## WSL Commands
compose_wsl_up:
	docker-compose -f docker-compose.yml -f docker-compose.wsl.yml up -d --build

compose_wsl_down:
	docker-compose -f docker-compose.yml -f docker-compose.wsl.yml down

compose_wsl_prod_up:
	docker-compose -f docker-compose.yml -f docker-compose.wsl.prod.yml up -d --build

compose_wsl_prod_down:
	docker-compose -f docker-compose.yml -f docker-compose.wsl.prod.yml down