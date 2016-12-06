from django.db.models import Q, F
from django.http import HttpResponse
from django.shortcuts import render
from tasks.models import Task

# Create your views here.
def show_tasks(request):

	#task_list = Task.objects.all()
	#result = "<br>".join([task.txt for task in task_list])

	#task_list = Task.objects.values_list("txt", flat=True)
	#result = "<br>".join(task_list)
	
	#task_list = Task.objects.filter(priority=2)

	#task_list = Task.objects.filter(priority__gte=2)
	#task_list = Task.objects.filter(txt__contains="go")

	#task_list = Task.objects.exclude(txt__contains="go")

	#task_list = Task.objects.filter(txt__contains="go", priority=2)

	#result = "<br>".join([task.txt for task in task_list])

	#q1 = Q(txt__contains="Do")

	#q2 = Q(priority__gt=2)

	#q = q1 | ~q2

	#task_list = Task.objects.filter(q)

	task_list = Task.objects.filter(time_given__gt=F("deadline"))

	result = "<br>".join([task.txt for task in task_list])

	return HttpResponse(result)




def show_task(request, task_id):
	t = Task.objects.get(id=task_id)
	return HttpResponse("<h1>%s</h1>" % t.txt)
