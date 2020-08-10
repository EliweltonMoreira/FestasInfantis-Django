from django.db import models
from temas.models import Tema


class Item(models.Model):
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
