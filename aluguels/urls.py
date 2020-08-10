from django.urls import path
from . import views

urlpatterns = [
    path('adicionar/<int:id>', views.adicionar, name='aluguel.adicionar'),
    path('editar/<int:id>', views.editar, name='aluguel.editar'),
    path('deletar/<int:id>', views.deletar, name='aluguel.deletar'),
]
