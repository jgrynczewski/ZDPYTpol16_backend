from django.shortcuts import render


# Create your views here.
def first(request):
    return render(
        request,
        'links/first.html',
    )

def second(request):
    return render(
        request,
        'links/second.html'
    )


def third(request, x):
    return render(
        request,
        'links/third.html',
        {"x": x}
    )
