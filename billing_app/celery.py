from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'billing_app.settings')

current_app = Celery('billing_app', include=['server_app.tasks'])
current_app.conf.enable_utc = False
current_app.conf.update(timezone='Asia/Kolkata')

current_app.config_from_object(settings, namespace='CELERY')

current_app.autodiscover_tasks()


# @current.task(bind=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')
