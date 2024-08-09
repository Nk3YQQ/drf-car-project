# Структура проекта
```
drf-car-project/
|—— config/ # Настройки проекта
    |—— __init__.py
    |—— asgi.py
    |—— settings.py
    |—— urls.py
    |—— wsgi.py
|—— nginx/ # Нстройка для образа nginx
    |—— Dockerfile
    |—— nginx.conf
|—— car/ # Приложение машин
    |—— migrations/  
    |—— __init__.py
    |—— admin.py
    |—— apps.py
    |—— models.py
    |—— serializers.py
    |—— urls.py
    |—— views.py
|—— users/ # Приложение пользователей
    |—— management/
    |—— migrations/
    |—— __init__.py
    |—— admin.py
    |—— apps.py
    |—— models.py
    |—— serializers.py
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
- ### Создано API для приложения и задокументирована в OpenAPI
- ### Разработан механизм аутентификации и авторизации происходит с помощью JWT Token и Bearer
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
