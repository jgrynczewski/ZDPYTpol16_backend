from django.urls import path

from new_app import views

urlpatterns = [
    path('/', views.hello),
    path('hi/', views.hi),
    path('adam/', views.adam),
    path('ewa/', views.ewa),
    path('new-year/', views.is_it_new_year),
    path('<str:name>/', views.display_name),
    path('2/<str:name>/', views.display_name2),
]