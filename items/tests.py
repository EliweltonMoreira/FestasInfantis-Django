from django.test import TestCase
from .models import Item
from temas.models import Tema


class ItemTestCase(TestCase):

    def setUp(self):
        for c in range(0, 5000):
            Item.objects.create(
                tema=Tema.objects.get(pk=15003),
                nome='Foice da Dona Morte',
                descricao='Foice decorativa de isopor da Dona Morte'
            )

    def test_performance(self):
        items = Item.objects.all()
        self.assertEquals(len(items), 5000)
