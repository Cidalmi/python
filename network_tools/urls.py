from django.urls import path

#from .views import HomePageView
from . import views

urlpatterns = [
    path('', views.index, name='index_network_tools'),
    path('spf', views.spf, name='spf'),
    path('dkim', views.dkim, name='dkim'),
    path('tracking', views.tracking, name='tracking'),
    path('return_path', views.return_path, name='return_path'),
    path('pages', views.pages, name='pages'),
    path('host', views.host, name='host'),
    #path('form', views.cadastrar_usuario, name='cadastrar_usuario'),
    
]
