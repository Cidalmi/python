from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('network_tools/', include('network_tools.urls')),
    path('bolsa/', include('bolsa.urls')),
    path('cep/', include('cep.urls')),
    path('', include('home.urls')),
]