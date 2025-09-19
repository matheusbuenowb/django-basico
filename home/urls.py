from django.urls import path
from . import views

urlpatterns = [
    #path('', home_views.home)
    path('', views.home) #outra forma mais generica de importar, é bom para padronizar imports entre apps
]
