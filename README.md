# Результаты тестирования

![Workflow Status](https://github.com/Nk3YQQ/drf-car-project/actions/workflows/main.yml/badge.svg)
[![Coverage Status](coverage/coverage.svg)](coverage/coverage-report.txt)

# Структура проекта
```
drf-car-project/
|—— cars/ # Приложение машин
    |—— migrations/  
    |—— __init__.py
    |—— admin.py
    |—— apps.py
    |—— filters.py
    |—— models.py
    |—— paginators.py
    |—— serializers.py
    |—— tests.py
    |—— urls.py
    |—— views.py
|—— config/ # Настройки проекта
    |—— __init__.py
    |—— asgi.py
    |—— settings.py
    |—— urls.py
    |—— wsgi.py
|—— coverage/ # Результаты тестирования
    |—— coverage.svg
    |—— coverage-report.txt
|—— nginx/ # Настройка для образа nginx
    |—— Dockerfile
    |—— nginx.conf
|—— users/ # Приложение пользователей
    |—— management/
    |—— migrations/
    |—— __init__.py
    |—— admin.py
    |—— apps.py
    |—— models.py
    |—— permissions.py
    |—— serializers.py
    |—— services.py
    |—— tests.py
    |—— urls.py
    |—— views.py
|—— .dockerignore
|—— .env.sample
|—— .flake8
|—— .gitignore
|—— docker-compose.dev.yml
|—— docker-compose.yml
|—— Dockerfile
|—— gunicorn_config.py
|—— LICENSE
|—— Makefile
|—— manage.py
|—— README.md
|—— requirements.txt
```

# Результаты работы:
- ### Реализован CRUD для машин и пользователей
- ### Приложение задокументировано в Swagger
- ### Разработан механизм аутентификации и авторизации с помощью JWT Token и Bearer
- ### Написаны тесты для API
- ### Реализован запуск приложения с помощью Docker, gunicorn и nginx
- ### Разработан механизм непрерывной интеграции (CI)

# Основной стек проекта:
- ### Python 3.10
- ### Django 4.2
- ### Django REST Framework 3.15
- ### PostgreSQL 11
- ### Django ORM
- ### gunicorn
- ### Docker
- ### GitHub Actions (CI)

# Как пользоваться проектом

## 1) Скопируйте проект на Ваш компьютер
```
git clone git@github.com:Nk3YQQ/drf-car-project.git
```

## 2) Добавьте файл .env для переменных окружения
Чтобы запустить проект, понадобятся переменные окружения, которые необходимо добавить в созданный Вами .env файл.

### С помощью pip
```
pip install -r requirements.txt
```

### С помощью poetry
```
poetry install
```

Пример переменных окружения необходимо взять из файла .env.sample

## 3) Запустите проект

Запуск проекта
```
make run
```

Остановка проекта
```
make stop
```
