import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'base.settings')

app = Celery('celery_app_name')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'example-task': {
        'task': 'main.tasks.example_task',
        'schedule': 2.0,  # every two seconds
        # 'schedule': crontab(minute=0, hour=0),  # by default UTC time zone
        'args': ('Hello world!',)
    },
}
