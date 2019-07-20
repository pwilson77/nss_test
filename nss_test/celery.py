
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nss_test.settings')
app = Celery('nss_test')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
