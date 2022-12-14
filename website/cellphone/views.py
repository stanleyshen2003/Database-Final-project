from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def home(request):
    return HttpResponse("Home page")

