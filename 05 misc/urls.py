from django.conf.urls import url
from tasks.views import show_task
from tasks.views import show_tasks
from tasks.views import update_task
from tasks.views import create_task

urlpatterns = [
    url(r'^(?P<task_id>\d+)$', show_task),
    url(r'^all$', show_tasks, name='all'),
    url(r'^(?P<task_id>\d+)/edit$',update_task,name="edit_task"),
    url(r'^create$',create_task,name='create')
]