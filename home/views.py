from django.http import HttpResponse
#from django.shortcuts import render

def home(request): ##view
    print("home")
    return HttpResponse('Home do app 1')