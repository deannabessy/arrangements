VENV := env
BIN := $(VENV)/bin
PYTHON := $(shell which python3)
PYTHON_VERSION_MIN=3.8
PYTHON_VERSION := $(shell $(PYTHON) -c 'import sys; print("%d.%d"% sys.version_info[0:2])' )
PYTHON_MINOR_VERSION := $(shell $(PYTHON) -c 'import sys; print(int(float("%d"% sys.version_info[1])))')
PYTHON_VERSION_OK := $(shell $(PYTHON) -c 'import sys;\
  print(int(float("%d.%d"% sys.version_info[0:2]) == $(PYTHON_VERSION_MIN)))' )

DOCKER_COMPOSE_RUN= docker-compose run --entrypoint="" --rm
DJANGO-MANAGE= python manage.py


ifeq ($(PYTHON_VERSION_OK),0)
  $(error "Your Python version is at $(PYTHON_VERSION), which is below the required $(PYTHON_VERSION_MIN).")
endif

default: build run

help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

venv:
	$(PYTHON) -m venv venv$(PYTHON_VERSION)

setup_local: ## install requirements if you want them locally. Do at your own risk; this was designed for a clean install of Ubuntu 20.04.4 LTS
	$(info please log out and then back in after this step for changes to take effect!)
	sudo apt update -y
	sudo apt upgrade -y
	$(PYTHON) -m pip install --upgrade pip
	pip install --upgrade -r requirements.txt
	sudo usermod -aG docker $(USER)

reqs: ## update requirements.txt
	pip freeze > requirements.txt

makemigrations: ## Make migrations
	$(DOCKER_COMPOSE_RUN) consumer $(DJANGO-MANAGE) makemigrations

migrate: ## apply migrations
	$(DOCKER_COMPOSE_RUN) consumer $(DJANGO-MANAGE) migrate

build: ## build the docker images (db, feed, consumer)
	docker-compose pull
	docker-compose build

stop: ## stop docker containers
	docker-compose stop 

run: makemigrations migrate stop ## Make migrations, apply them, stop containers from migrations, bring up db, feed, & consumer containers
	docker-compose up -d

restart: ## stop then run the stack
	stop run

lint: ## run flake8 & black
	$(DOCKER_COMPOSE_RUN) consumer flake8
	$(DOCKER_COMPOSE_RUN) black 

createsuperuser: ## Add a superuser to the Django app
	$(DOCKER_COMPOSE_RUN) consumer $(DJANGO-MANAGE) createsuperuser
