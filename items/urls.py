from django.urls import path
from . import views

urlpatterns = [
    path('adicionar/<int:id>', views.adicionar, name='item.adicionar'),
    path('editar/<int:id>', views.editar, name='item.editar'),
    path('deletar/<int:id>', views.deletar, name='item.deletar'),
]
