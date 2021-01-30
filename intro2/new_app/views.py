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
    return HttpResponse("Witaj, Ewa!")


def display_name(request, name):
    sanitize_name = escape(name)
    return HttpResponse(f"Witaj, {sanitize_name}!")
