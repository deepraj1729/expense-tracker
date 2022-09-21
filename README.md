# Expense-Tracker
An expense tracker built with FARM stack (FastAPI,React,MongoDB)

![frontend](media/frontend.png)

## Requirements
- Docker
- Docker-Compose

## Install and Run
To install and run the application, use `docker-compose` as given below:

1. `Build`: To build the application (api+frontend+db):

        docker-compose up -d --build

2. `Delete or Remove`: To delete or remove the containers (api+frontend+db):

        docker-compose down


> A demo CLI after running `docker-compose`
![cli](media/cli.png)


> Shut application
![makefile](media/makefile.png)


> Running Containers
![docker](media/docker.png)


## Environments
There are two environments as of now, `development` and `production`

1. `Development`:
- Build:

        docker-compose up -d --build

> To make this command easier using Makefile:

        make compose_up

- Delete or Remove:

        docker-compose down

> To make this command easier using Makefile:

        make compose_down

2. `Production`:
- `Build`: To build it for production using `react-multistage` builds and `nginx`

        docker-compose -f docker-compose.prod.yml up -d --build

> To make this command easier

        make compose_prod_up

- `Delete or Remove`: To remove the running containers

        docker-compose -f docker-compose.prod.yml down

> To make this command easier

        make compose_prod_down

## Architecture
The architecture of the backend is as follows:

- API Framework: `FastAPI`
- ORM (Object Relational Mapper): `Python Class Abstraction`
- API Query framework: `GraphQL`
- DB: `MongoDB`
- DB Driver: `Pymongo`
- Cache: `Redis`
- CI/CD: `Github Actions`
- Container: `Docker`
- Workflow: `Docker-Compose`

## Services and PORTS:
The services running are:
- api (`fastapi`)
- frontend (`react`)
- db (`mongodb`)

The ports running these services on:
> Development Env:
- api: `localhost:8000`
- frontend: `localhost:3000`
- db: `localhost:27017`

> Production Env:
- api: `localhost:8000`
- frontend: `localhost:4000`
- db: `localhost:27017`


## API Documentation:

> Dashboard:
- Overall Dashboard: GET `/dashboard/all`
- Monthly Dashboard: GET `/dashboard/{month_name}`

> Transactions:
- All Transactions: GET `/transaction/all`
- Get Transaction by ID: GET `/transaction/{id}`
- Get Transactions by Month: GET `/transactions/{month}`
- Add a Transaction: POST `/transaction/add`
- Delete a Transaction by ID: DELETE `/transaction/{id}`
- Delete entire Table/Collection: DELETE `/transactions`