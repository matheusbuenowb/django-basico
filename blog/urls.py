from django.urls import path
#from home import views as home_views

from . import views

#blog/  -> já está incluido aqui

app_name = 'blog' #namespace para urls

urlpatterns = [
    #path('', home_views.home)
    path('', views.blog, name = 'blog'), #outra forma mais generica de importar, é bom para padronizar imports entre apps
    path('exemplo/', views.exemplo, name ='exemplo'),
    path('post/<int:post_id>/', views.post, name ='post') #mudei de blog para post: assim envia conflitos
    #e conserta o erro de views com 2 parametros [request, id]
    #int é para converter o id em inteiro e nao permitir strings
]
