from django.db import models


class Tema(models.Model):
    nome = models.CharField(max_length=255)
    valorAluguel = models.DecimalField(max_digits=8, decimal_places=2)
    corDestaque = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
