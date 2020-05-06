from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kt_team_test.settings')

app = Celery('proj', broker='redis://redis/0', backend='redis://redis/0')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
