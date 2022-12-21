from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
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

def register(request):
    if request.method == 'POST':
        id = request.POST['id']
        age = request.POST['age']
        gender = request.POST['gender']
        occupation = request.POST['occupation']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if Users.objects.filter(id=id).exists():
                messages.info(request, 'Username Alredy Used')
                return redirect('register')
            else:
                user = Users(username = id,age = age, gender = gender, occupation = occupation, password = password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password Not The Same.')
            return redirect('register')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        id = request.POST['id']
        password = request.POST['password']
        if Users.objects.filter(id = id, password = password).exists():
            messages.info(request, 'Credentials Invalid')
            return redirect('login')
        else:
            return redirect('/')
    return render(request, 'login.html')