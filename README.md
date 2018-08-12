# Django Celery Redis example #

Basic project setup for Django + Celery + Redis

## Modified modules ##
- base/celery.py
- base/settings.py
- main/\_\_init__.py
- main/tasks.py

## Install ##
```sh
pip install -r requirements.txt
```

## Start ##
```sh
celery worker --app main --loglevel info --beat
```