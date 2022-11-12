# FoodGram Web-Site

[![Workflow status](https://github.com/gasimovv21/foodgram-project-react/actions/workflows/main.yml/badge.svg)](http://cook-teach.sytes.net/recipes)

## **Описание**
- Вы человек который любит вкусно поесть и готовить? ✨
- Любите делиться своими рецептами? 🤔
- фастфуд ? Веган ? ЗОЖ? 🤓
- Вы пришли прямо по адресу, теперь на просторах интернета есть проект FoodGram где каждому человеку найдётся своё место и любимое блюдо. 🥳
- Food-Gram. «Продуктовый помощник»: сайт, на котором каждый пользователь может публиковать свои замечательние рецепты, добавлять чужие рецепты в избранное и подписываться на других авторов чтобы следить за рецептами. Сервис «Список покупок» позволит пользователям создавать список продуктов, которые нужно купить для приготовления выбранных блюд.💥
 
### 1) Инструкция по установке:

## Локальная установка:
- Клонируем репозиторию на компьютер:

```bash
1) git@github.com:gasimovv21/foodgram-project-react.git
2) cd foodgram-project-react
```

- Cоздать и активировать виртуальное окружение:

```bash
python -m venv venv
```

```bash
source venv/Scripts/activate - Windows

source venv/bin/activate - Linux systems
```
- Установить зависимости проекта:

```bash
cd backend/

pip install -r requirements.txt
```

- Создать и выполнить миграции:
```bash
python manage.py makemigrations
python manage.py migrate
```

- Запуск сервера локально:
```bash
python manage.py runserver
```

## Наполнение файла env:
```
SECRET_KEY = example(свой ключ, ниже способ как сгенерировать ключ. 🔻)
```
```
from django.core.management.utils import get_random_secret_key
get_random_secret_key()
```
```
DB_ENGINE=django.db.backends.postgresql 
```
```
DB_NAME=example (назовите свой)
```
```
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

### 2) Настройки для Deploy

В настройках вашего проекта на GitHub Settings->Security->Secrets->Actions нажав кнопку (New repository secret) создадите ниже перечисленные секреты.

```
1) DOCKER_USERNAME - Логин от DockerHub https://docs.docker.com/engine/reference/commandline/login/
2) DOCKER_PASSWORD - Пароль от DockerHub
3) HOST - IP Адрес вашего сервера
4) USER - Ммя пользователя для подключения к серверу
5) PASSPHRASE - Если при создании ssh-ключа вы использовали фразу-пароль, то напишите
6) SSH_KEY - Приватный ssh-ключ получить можно по команде в терминале cat ~/.ssh/id_rsa
7) SECRET_KEY - Секретный ключ
8) DEBUG - Дебаг
7) DB_ENGINE - Указываем, что работаем с postgresql
8) DB_NAME - Имя базы данных
7) POSTGRES_USER - Логин для подключения к базе данных
8) POSTGRES_PASSWORD - Пароль для подключения к БД
7) DB_HOST - Название сервиса (контейнера)
8) DB_PORT - Порт для подключения к БД
```

### После того как деплой и тесты на платформе прошли успешно подключаемся к серверу и вводим команды ниже:

1) Создать миграции и применить:

```
sudo docker-compose exec backend python manage.py makemigrations --noinput

sudo docker-compose exec backend python manage.py migrate --noinput
```

2) Собирать статику:

```
sudo docker-compose exec backend python manage.py collectstatic --noinput
```

3) Создать суперпользователя:

```
sudo docker-compose exec backend python manage.py createsuperuser
```

4) Пока что в базе данных пусто, так чего ждём?) Загружаем ингредиенты и теги:

```
sudo docker-compose exec -T backend python manage.py loaddata data/ingredients.json 

sudo docker-compose exec -T backend python manage.py loaddata data/tags.json 
```

5) Открываем прооект по сыллке - http://cook-teach.sytes.net/

## Технологий которыми пользовался при разработке

- Python
- Django
- DRF
- GitHubActions
- PostgreSQL
- Nginx
- Docker
- Yandex.Cloud

### _**Автор:**_

- _**Эльтун Гасимов 👨‍💻 - https://github.com/gasimovv21**_

# **Поддержали при разработке:**

- **Яндекс Практикум 👨‍💻 - https://practicum.yandex.ru/**
