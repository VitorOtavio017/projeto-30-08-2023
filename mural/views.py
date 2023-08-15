
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import admin
from .models import Mural
# Create your views here.


def index(request):
    return render(request, 'pages/index.html', context={
    })
def login(request):
    return render(request, 'pages/login.html', context={
    })
# def register(request):
#     if request.POST:
#       form = RegisterForm(request.POST)
#     else:
#        form = RegisterForm()
#     return render(request, 'pages/register.html', context={
#         'form': form,
#     })

def register(request):
     return render(request, 'pages/register.html', context={
     })
def mycards(request):
    return render(request, 'pages/mycards.html', context={
    })
def menu(request):
    return render(request, 'pages/menu.html', context={
    })
def sobre(request):
    return render(request, 'pages/sobre.html', context={
    })
