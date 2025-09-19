from django.http import HttpResponse
# from django.shortcuts import render

def blog(request):  ##view
    print('blog')
    return HttpResponse('blog do app 1')

def exemplo(request):
    print('exemplo')
    return HttpResponse('exemplo 1')