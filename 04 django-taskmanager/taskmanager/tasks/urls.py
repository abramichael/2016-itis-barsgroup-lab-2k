from django.conf.urls import url
from tasks.views import *

urlpatterns = [
    url(r'^all$', show_tasks),
    url(r'^(?P<task_id>\d+)', show_task),
]