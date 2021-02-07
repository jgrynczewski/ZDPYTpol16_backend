from django.shortcuts import render

from form_app3.models import Task


# Create your views here.
def register(reqeust):
    return render(
        reqeust,
        'form_app3/register.html',
    )


def task_list(request):

    task = request.POST.get('task')

    if task:
        Task.objects.create(name=task)

        # Alternatywnie
        # Task(name=task).save()

    tasks = Task.objects.all()

    return render(
        request,
        "form_app3/task_list.html",
        context={
            "tasks": tasks
        }
    )
