from django.http import HttpResponse
from django.shortcuts import render

def blog(request): ##view
    print("blog")

    context = {
        'text': 'Olá blog',
        'title': 'Página de Blog - '
    }

    
    return render(
        request,
        'blog/index.html',
        context
    )

def exemplo(request):
    print('exemplo')
    return HttpResponse('exemplo 1')