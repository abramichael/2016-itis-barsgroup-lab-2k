import time
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect as Redirect
from django.urls import reverse
from django.urls import reverse_lazy
from tasks.models import Task
from tasks.forms import TaskForm, TaskFormEdit


def show_task(request, task_id):

    t = Task.objects.get(id=task_id)

    return HttpResponse("Hi, task :  %s" % t)


def show(request):
    # task_list = Task.objects.filter(txt__contains="Do")

    # task_list = Task.objects.exclude(txt__contains="Do")

    q1 = Q(txt__contains="Do")

    q2 = Q(priority__gte=2)

    q = q1 | q2

    task_list = Task.objects.filter(time_given__lt=F("deadline"))

    result = "br".join([task.txt for task in task_list])

    return HttpResponse(str(result))


def show_tasks(request):

    tasks = Task.objects.all()

    args = {"tasks": tasks}

    return render(request, "tasks/show.html", args)


@login_required(login_url=reverse_lazy('login'))
def update_task(request, task_id):
    if 'edit10' in request.session:
        if time.time() - request.session['edit10'] < 10:
            return Redirect(reverse('tasks:all'))
        else:
            request.session["edit10"] = time.time()
    else:
        request.session['edit10'] = time.time()
    if request.method == "POST":
        task = Task.objects.get(id=task_id)
        t = TaskFormEdit(request.POST, instance=task)
        t.save()
        return Redirect(reverse('tasks:all'))
    elif request.method == "GET":
        task = Task.objects.get(id=task_id)
        f = TaskFormEdit(instance=task)
        return render(request, "tasks/update.html", {"f": f})
    else:
        return HttpResponse("Method is not supported")

def create_task(request):

    if request.user.is_authenticated():
        args = {}
        if request.POST:
            f = TaskForm(request.POST)
            f.save()
            Redirect(reverse('tasks:all'))

        args['form'] = TaskForm()
        return render(request, "tasks/create.html", args)
    else:
        return Redirect(reverse('login'))


def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,
                            password=password)
        if user is not None:
            auth_login(request, user)
            return Redirect(reverse('tasks:all'))
        else:
            return Redirect(reverse('login'))
    else:
        return render(request, 'login.html')
