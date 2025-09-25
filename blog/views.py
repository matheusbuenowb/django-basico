from django.http import HttpResponse, HttpRequest, Http404
from django.shortcuts import render
from blog.data import posts #importamos os dados posts ficticios
from typing import Any

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

def post(request: HttpRequest, post_id: int): ##view para casos com id, e força tipagem do tipo inteiro

    found_post: dict[str, Any] | None = None #inicialmente nulo ou post encontrado tipado do tipo dicionario

    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break #ajuda a nao continuar o loop desnecessariamente

    if found_post is None:
        raise Http404('Post não encontrado') #agora sim, se n achar o post, retorna 404

    print("post: ", id)

    context = {
        'id': id,
        'text': 'Olá blog', 
        'post': found_post, #dai aqui ele pega o post relacionado ao id
        'title':found_post['title']
    }

    
    return render(
        request,
        'blog/post.html',
        context
    )

def exemplo(request):
    print('exemplo')
    return HttpResponse('exemplo 1')