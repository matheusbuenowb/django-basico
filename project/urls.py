from django.contrib import admin
from django.urls import path, include
#from home import views as home_views
#from blog import views as blog_views

#Model, view, controller

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')), #feito aninhamento blog
    path('', include('home.urls')) #feito aninhamento home
]
