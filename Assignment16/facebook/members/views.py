from django.shortcuts import render
from django.http import HttpResponse

def members(request):
    return HttpResponse("<h1 style=color:Blue;>Hello World!</h1>")
