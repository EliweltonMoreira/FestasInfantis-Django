from django.contrib import admin
from django.urls import path, include
from temas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.welcome, name='welcome'),
    path('tema/', include('temas.urls')),
    path('item/', include('items.urls')),
    path('cliente/', include('clientes.urls')),
    path('aluguel/', include('aluguels.urls')),
    path('accounts/', include('users.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
