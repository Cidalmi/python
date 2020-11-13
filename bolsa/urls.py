from django.urls import path
from . import views

urlpatterns = [  
    path('', views.bolsa, name='bolsa'),
    path('get_dados_bolsa', views.get_dados_bolsa, name='get_dados_bolsa'),
    
]