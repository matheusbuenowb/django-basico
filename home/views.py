from django.http import HttpResponse
from django.shortcuts import render

def home(request): ##view
    print("home")
    return render(
        request, 'home/index.html'
    )