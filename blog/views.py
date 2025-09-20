from django.http import HttpResponse
from django.shortcuts import render

def blog(request): ##view
    print("blog")
    return render(
        request, 'blog/index.html'
    )

def exemplo(request):
    print('exemplo')
    return HttpResponse('exemplo 1')