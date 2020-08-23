from django.test import TestCase
from .models import Cliente


class ClienteTestCase(TestCase):

    def setUp(self):
        for c in range(0, 5000):
            Cliente.objects.create(
                nome='SHA',
                telefone='(81) 99324-7653'
            )

    def test_performance(self):
        clientes = Cliente.objects.all()
        self.assertEquals(len(clientes), 5000)
