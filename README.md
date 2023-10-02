# FoodGram Web-Site

[![Workflow status](https://github.com/gasimovv21/foodgram-project-react/actions/workflows/main.yml/badge.svg)](http://cook-teach.sytes.net/recipes)

## **Description**
- Are you a person who likes to eat delicious food and cook? ✨
- Do you like to share your recipes? 🤔
- fast food ? Vegan ? Healthy lifestyle? 🤓
- You have come right to the address, now there is a FoodGram project on the Internet where everyone will find their place and favorite dish. 🥳
- Food-Gram. "Grocery Assistant": a website where each user can publish their wonderful recipes, add other people's recipes to favorites and subscribe to other authors to follow the recipes. The Shopping List service will allow users to create a list of products that they need to buy to prepare selected dishes.💥

### 1) Installation Instructions:

## Local installation:
- Clone the repository to a computer:

```bash
1) git@github.com:gasimovv21/foodgram-project-react.git
2) cd foodgram-project-react
```

- Create and activate a virtual environment:

```bash
python -m venv venv
```

```bash
source venv/Scripts/activate - Windows

source venv/bin/activate - Linux systems
``
- Install project dependencies:

```bash
cd backend/

pip install -r requirements.txt
```

- Create and perform migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

- Running the server locally:
``bash
python manage.py runserver
``

## Filling the env file:
``
SECRET_KEY = example(your key, below is a way to generate a key. 🔻)
```
```
from django.core.management.utils import get_random_secret_key
get_random_secret_key()
```
```
DB_ENGINE=django.db.backends.postgresql

`` ``
DB_NAME=example (name your
own)
`` ``
POSTGRES_USER=example
```
```
POSTGRES_PASSWORD=postgres
```
```
DB_HOST=db
```
```
DB_PORT=5432
```

###2) Settings for Deploy

In the settings of your project on GitHub Settings->Security->Secrets->Actions, click (New repository secret) to create the secrets listed below.

```
1) DOCKER_USERNAME - Login from DockerHub https://docs.docker.com/engine/reference/commandline/login/
2) DOCKER_PASSWORD - Password from DockerHub
3) HOST - IP Address of your server
4) USER - The number of the user to connect to the server
5) PASSPHRASE - If you used a passphrase when creating an ssh key, then write
6) SSH_KEY - A private ssh key can be obtained by command in the terminal cat ~/.ssh/id_rsa
7) SECRET_KEY - Secret key
8) DEBUG - Debug
7) DB_ENGINE - Indicate that we are working with postgresql
8) DB_NAME - Database name
7) POSTGRES_USER - Login to connect to the database
8) POSTGRES_PASSWORD - Password for connecting to the database
7) DB_HOST - Name of the service (container)
8) DB_PORT - The port for connecting to the database
```

### After the deployment and tests on the platform have passed successfully, we connect to the server and enter the commands below:

1) Create migrations and apply:

```
sudo docker-compose exec backend python manage.py makemigrations --noinput

sudo docker-compose exec backend python manage.py migrate --noinput
```

2) Collect static:

```
sudo docker-compose exec backend python manage.py collectstatic --noinput
```

3) Create a superuser:

```
sudo docker-compose exec backend python manage.py createsuperuser
```

4) So far, the database is empty, so what are we waiting for?) Uploading ingredients and tags:

```
sudo docker-compose exec -T backend python manage.py loaddata data/ingredients.json 

sudo docker-compose exec -T backend python manage.py loaddata data/tags.json 
```

5) We open the project by sending - http://cook-teach.sytes.net/

## Of technologies used during development

- Python
- Django
- DRF
- GitHubActions
- PostgreSQL
- Nginx
- Docker
- Yandex.Cloud

### _**Author:**_

- _**Eltun Gasimov 👨💻 - https://github.com/gasimovv21**_

# **Supported during development:**

- **Yandex Practicum 👨💻 - https://practicum .yandex.ru/**
