from django.http import HttpResponse
from django.shortcuts import render

def home(request): ##view
    print("home")


    context = {
        'text': 'Olá home'
    }


    return render(
        request,
        'home/index.html',
        context
    )