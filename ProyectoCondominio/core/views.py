from django.shortcuts import render,redirect
from django.http import HttpResponse
#from django.contrib.auth.decorators import login_required


# Create your views here.
#@login_required

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def vistaresidente(request):
    return render(request, 'vistaresidente.html')

def pagoresidente(request):
    return render(request, 'pagoresidente.html')