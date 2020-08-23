from django.test import TestCase
from .models import Tema


class TemaTestCase(TestCase):

    def setUp(self):
        for c in range(0, 5000):
            Tema.objects.create(
                nome='Penadinho',
                valorAluguel=1499.90,
                corDestaque='Branco'
            )

    def test_performance(self):
        temas = Tema.objects.all()
        self.assertEquals(len(temas), 5000)
