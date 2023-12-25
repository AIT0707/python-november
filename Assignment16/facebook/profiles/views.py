from django.shortcuts import render
from django.http import HttpResponse

def profiles(request):
    return HttpResponse("<h1>Profile</h1><p>First name: Ikrom <br>Last name: Abdullaev <br>Age: 33 <br>Phone: +992111700707<br>Email: <a href=ikrom.abdullaev@ucentralasia.org>ikrom.abdullaev@ucentralasia.org</a></p>")
