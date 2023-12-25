from django.shortcuts import render
from django.http import HttpResponse

def cities(request):
    return HttpResponse("<h1> Tajikistan big cities are: <br> Dushanbe <br>Khudjand <br>Kulob </h1>")
    
