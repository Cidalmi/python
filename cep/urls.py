from django.urls import path

#from .views import HomePageView
from . import views

urlpatterns = [
    path('', views.index, name='home_cep'),    
    
]
