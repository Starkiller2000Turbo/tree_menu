ifeq ($(OS),Windows_NT)
    PYTHON = python
	PIP = pip
else
    PYTHON = python3
	PIP = pip3
endif

WORKDIR = tree_menu
TEMPLATES-DIR = $(WORKDIR)/templates
MANAGE = $(PYTHON) $(WORKDIR)/manage.py
BASE_MANAGE = $(PYTHON) manage.py

default:
	$(MANAGE) makemigrations
	$(MANAGE) migrate
	$(MANAGE) runserver

begin:
	$(MANAGE) makemigrations;
	$(MANAGE) migrate;
	$(MANAGE) createsuperuser --noinput;
	$(MANAGE) runserver

style:
	isort $(WORKDIR)
	black -S -l 79 $(WORKDIR)
	flake8 $(WORKDIR)
	djlint $(TEMPLATES-DIR) --reformat --indent 2
	mypy $(WORKDIR)

pip:
	$(PYTHON) -m pip install --upgrade pip

venv:
	$(PYTHON) -m venv venv

req:
	$(PIP) install -r requirements.txt

style-req:
	$(PIP) install -r requirements-style.txt

project:
	django-admin startproject $(name)

app: 
	cd $(WORKDIR); \
	$(BASE_MANAGE) startapp $(name); \
	cd ..

migrations:
	$(MANAGE) makemigrations

migrate:
	$(MANAGE) migrate

superuser:
	$(MANAGE) createsuperuser

fastuser:
	$(MANAGE) createsuperuser --noinput

run:
	$(MANAGE) runserver

static:
	$(MANAGE) collectstatic

secret-key:
	$(MANAGE) generate_key
