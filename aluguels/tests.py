from django.test import TestCase
from .models import Aluguel
from clientes.models import Cliente
from temas.models import Tema
from datetime import date, time


class AluguelTestCase(TestCase):

    def setUp(self):
        for c in range(0, 5000):
            Aluguel.objects.create(
                cliente=Cliente.objects.get(pk=15020),
                tema=Tema.objects.get(pk=15003),
                dataFesta=date(2020, 11, 30),
                horarioInicio=time(19, 00, 00),
                horarioTermino=time(23, 00, 00),
                valorCobrado=2099.90,
                endereco='Rua Oliveira, 123',
                complemento='Casa',
                cidade='Ferreiros',
                uf='Pernambuco'
            )

    def test_performance(self):
        aluguels = Aluguel.objects.all()
        self.assertEquals(len(aluguels), 5000)
