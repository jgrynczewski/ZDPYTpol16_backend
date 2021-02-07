from django.shortcuts import render
from django.shortcuts import Http404
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist

from form_app4.models import Task

# Create your views here.
def register(request):
    return render(
        request,
        "form_app4/register.html"
    )


def task_list(request):

    if request.method == "POST":
        task = request.POST.get('task')

        if task:
            Task.objects.create(name=task)
        return redirect("form4:task_list")

    tasks = Task.objects.all()

    return render(
        request,
        'form_app4/task_list.html',
        {"tasks": tasks}
    )


def update(request, task_id):

    if request.method == "GET":
        # task = Task.objects.filter(id=task_id).first()
        # task = Task.objects.get(id=task_id)
        #
        # try:
        #     task = Task.objects.get(pk=task_id)
        # except ObjectDoesNotExist:
        #     raise Http404

        task = get_object_or_404(Task, id=task_id)

        return render(
            request,
            'form_app4/update.html',
            {"task": task}
        )

    if request.method == "POST":
        modified_task = request.POST.get('task')

        if modified_task:
            # task = Task.objects.filter(id=task_id).first()
            # task = Task.objects.get(id=task_id)
            # task = Task.objects.get(pk=task_id)
            task = get_object_or_404(Task, id=task_id)

            task.name = modified_task
            task.save()

        tasks = Task.objects.all()

        # return render(
        #     request,
        #     'form_app4/task_list.html',
        #     {"tasks": tasks},
        # )
        return redirect("form4:task_list")