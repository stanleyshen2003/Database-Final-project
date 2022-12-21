from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import Users
from .models import Data
from .models import Rate

def home(request):
    return render(request, 'main.html')

def get_users(request):
    users = Users.objects.all()
    return render(request, 'users.html', {'users':users})

def get_data(request):
    data = Data.objects.all()
    return render(request, 'data.html', {'data':data})

def get_rate(request):
    rate = Rate.objects.all()
    return render(request, 'rate.html', {'rate':rate})
