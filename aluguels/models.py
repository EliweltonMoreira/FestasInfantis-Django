from django.db import models
from clientes.models import Cliente
from temas.models import Tema


class Aluguel(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE)
    dataFesta = models.DateField()
    horarioInicio = models.TimeField()
    horarioTermino = models.TimeField()
    valorCobrado = models.DecimalField(max_digits=8, decimal_places=2)
    endereco = models.CharField(max_length=255)
    complemento = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    uf = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.endereco
