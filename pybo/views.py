from django.shortcuts import render
from .models import Home
from django.http import HttpResponse

def index(request):
    return render(request, 'base.html')