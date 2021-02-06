from django.shortcuts import render

# Create your views here.
def register(reqeust):
    return render(
        reqeust,
        'form_app2/register.html',
    )


def task_list(request):

    with open('tasks.txt', 'a+') as f:
        task = request.POST.get('task')

        if task:
            f.write(task+"\n")

    with open('tasks.txt', 'r') as f:
        tasks = f.readlines()

    return render(
        request,
        "form_app2/task_list.html",
        context={
            "tasks": tasks
        }
    )
