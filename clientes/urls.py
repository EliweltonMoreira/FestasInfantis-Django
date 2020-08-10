from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='cliente.index'),
    path('detalhe/<int:id>', views.detalhe, name='cliente.detalhe'),
    path('adicionar/', views.adicionar, name='cliente.adicionar'),
    path('editar/<int:id>', views.editar, name='cliente.editar'),
    path('deletar/<int:id>', views.deletar, name='cliente.deletar'),
]
