"""intro2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('hello1/', views.hello1),
    # path('hello2/', views.hello2),
    # path('hello3/', views.hello3),
    # path('new/', views.new),
    path('new_app/', include('new_app.urls')),
    path('links/', include('links.urls')),
    path('inheritance/', include('inheritance.urls')),
    path('form_app/', include('form_app.urls')),
    path('form_app2/', include('form_app2.urls')),
    path('form_app3/', include('form_app3.urls')),
    path('form_app4/', include('form_app4.urls')),
]
