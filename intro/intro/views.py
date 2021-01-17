from django.shortcuts import HttpResponse

def hello(request):
    return HttpResponse("<!DOCTYPE html><html><head><meta charset='utf-8'><title>Moja strona</title></head><body>OK</body></html>")