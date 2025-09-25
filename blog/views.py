from django.http import HttpResponse
from django.shortcuts import render
from blog.data import posts #importamos os dados posts ficticios

def blog(request): ##view
    print("blog")

    context = {
        'text': 'Olá blog',
        'posts': posts
    }

    
    return render(
        request,
        'blog/index.html',
        context
    )

def exemplo(request):
    print('exemplo')
    return HttpResponse('exemplo 1')