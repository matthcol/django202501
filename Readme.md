# Django

## Install
pip install django
pip install mssql-django
pip install django-extensions

## Start Project
```
mkdir movieproject
django-admin startproject moviesite movieproject
```

Result:
```
── movieproject
    ├── manage.py
    └── moviesite
        ├── __init__.py
        ├── asgi.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py
```

## Run server
python .\manage.py runserver

## Create app
python manage.py startapp movieapp

## Migrations
python manage.py showmigrations
python manage.py showmigrations movieapp

python manage.py makemigrations movieapp

python manage.py sqlmigrate movieapp 0001 > sql/0001_movie_ddl.sql

python manage.py showmigrations
python manage.py migrate admin
... + auth + contenttypes + sessions
python manage.py migrate movieapp

Revert migrations
python manage.py migrate movieapp 0001
python manage.py migrate movieapp zero

## django shell
### default shell
python .\manage.py shell
### with GUI lab or notebook
python .\manage.py shell_plus --lab
python .\manage.py shell_plus --notebook

NB: set environment variable DJANGO_ALLOW_ASYNC_UNSAFE

#### Command Dos
```
set DJANGO_ALLOW_ASYNC_UNSAFE=True
```

#### Powershell
```
${env:DJANGO_ALLOW_ASYNC_UNSAFE}="True"
```

#### Bash
```
export DJANGO_ALLOW_ASYNC_UNSAFE=True
```

### Templates
- template ref: https://docs.djangoproject.com/en/5.1/ref/templates/
- builtin tags and filters: https://docs.djangoproject.com/en/5.1/ref/templates/builtins/
- custom tags and filters: https://docs.djangoproject.com/en/5.1/howto/custom-template-tags/

