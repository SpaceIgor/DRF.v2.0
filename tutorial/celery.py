import os
from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tutorial.settings')

app = Celery('tutorial')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'change_author_status': {
        'task': 'tutorial.qiuckstart.tasks.change_author_status',
        'schedule': crontab(minute=0, hour=0),
    },
}