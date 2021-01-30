from django.shortcuts import HttpResponse
from django.shortcuts import render

#Widok - funkcja przyjmująca zapytanie HTTP i zwracająca odpowiedź HTTP
def hello1(request):
    return HttpResponse("Hello, world!")


def hello2(request):
    return HttpResponse("<!DOCTYPE html><html><head></head><body><h3>Hello, world!</h3></body></html>")


def hello3(request):
    return render(request, 'templates/hello.html')


def new(request):
    return render(request, 'templates/new.html')

