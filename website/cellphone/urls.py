from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('users/', views.get_users),
    path('rate/', views.get_rate),
    path('data/', views.get_data),
    path('login/', views.login),
    path('register/', views.register),
]
