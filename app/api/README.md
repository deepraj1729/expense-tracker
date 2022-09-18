# Xpense-Backend
Xpense by Limebrew powered by FastAPI

![code](media/code.png)

## Requirements
- Conda
- Bash/Zsh
- MongoDB
- .env file consisting the `DATABASE_CONN_URL` environment variable

## Installation
- `Method 1` Setup environment and install using conda and pip:
    
        conda create -n "xpense" python=3.9
        conda activate "xpense"
        pip install -r requirements.txt

- `Method 2` Setup environment and install using script (bash script):

        bash install.sh

- `Method 3` Setup environment using Makefile with `install` trigger:

        make install

## MongoDB
Run `MongoDB` locally for development using `Docker`:

        docker run -d -p 27017:27017 --name xpense-db mongo

## Run Application
- `Method 1` Using uvicorn (installed with requirements.txt):

        uvicorn main:app --reload

- `Method 2` Using script (bash script):

        bash run.sh

- `Method 3` Using Makefile with `run` trigger:

        make run

- `Method 4` To run with a clean environment:

        make clean_run


## Docker-Compose:
To make workflows and applications configuration easier,docker-compose is used. Here is how it's done:

1. To build the application (api+db):

        docker-compose up -d --build

> To make this command easier

        make compose_up

2. To delete or remove the containers (api+db):

        docker-compose down

> To make this command easier

        make compose_down

![docker-compose](media/terminal.png)

![docker](media/docker.png)



## Uninstallation
- `Method 1` Using conda:

        conda env remove -n "xpense"

- `Method 2` Using script (bash script):

        bash uninstall.sh

- `Method 3` Using Makefile:

        make uninstall

## Architecture
The architecture of the backend is as follows:

- API Framework: `FastAPI`
- ORM (Object Relational Mapper): `python Class Abstraction`
- API Query framework: `GraphQL`
- DB: `MongoDB`
- Cache: `Redis`
- CI/CD: `Github Actions`
- Container: `Docker`
- Workflow: `Docker-Compose`


## API Documentation
Tool used: Swagger

![api](media/api.png)

## API Testing

## Deployment

## Monitoring & Logs

