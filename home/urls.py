from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog', views.post_list, name='post_list'),
    path('network_tools', views.post_list, name='network_tools'),
]