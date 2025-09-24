from django.urls import path
from . import views

app_name = 'home' #namespace para urls

urlpatterns = [
    #path('', home_views.home)
    path('', views.home, name = 'home') #outra forma mais generica de importar, é bom para padronizar imports entre apps
    #feito dinamicamente, muito melhor
]
