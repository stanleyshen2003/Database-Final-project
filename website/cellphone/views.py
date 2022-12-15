from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import Users

def home(request):
    return HttpResponse("Home page")

def get_users(request):
    userss = Users.objects.all()
    return render(request, 'home.html', {'users':userss})