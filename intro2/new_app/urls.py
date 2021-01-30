from django.urls import path

from new_app import views

urlpatterns = [
    path('/', views.hello),
    path('hi/', views.hi),
    path('adam/', views.adam),
    path('ewa/', views.ewa),
    path('<str:name>/', views.display_name),
]