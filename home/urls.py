from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('blog', views.post_list, name='post_list'),
    #path('network_tools', views.network_tools, name='network_tools'),
    #path('bolsa', views.bolsa_familia, name='bolsa'),
    path('post_email', views.post_email, name='post_email'),

]