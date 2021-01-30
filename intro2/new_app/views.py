import datetime

from markupsafe import escape

from django.shortcuts import HttpResponse
from django.shortcuts import render


# Create your views here.
def hello(request):
    return HttpResponse("OK")


def hi(request):
    return render(request, "new_app/hello.html")


def adam(request):
    return HttpResponse("Witaj, Adam!")


def ewa(request):
    return HttpResponse("Witaj, Ewa!aaaaaa")


def display_name(request, name):
    sanitize_name = escape(name)
    return HttpResponse(f"Witaj, {name}!")


def display_name2(request, name):
    return render(
        request,
        'new_app/name.html',
        context={"name": name}
    )


def is_it_new_year(request):
    now = datetime.datetime.now()
    is_new_year = now.day==30 and now.month==1
    return render(request, 'new_app/is_it_newyear.html', {"is_new_year": is_new_year})

