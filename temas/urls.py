from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='tema.index'),
    path('detalhe/<int:id>', views.detalhe, name='tema.detalhe'),
    path('adicionar/', views.adicionar, name='tema.adicionar'),
    path('editar/<int:id>', views.editar, name='tema.editar'),
    path('deletar/<int:id>', views.deletar, name='tema.deletar'),
]
