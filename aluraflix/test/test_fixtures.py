from django.test import TestCase
from aluraflix.models import Programa

class FixturesDataTestCase(TestCase):
    fixtures = ['programas_iniciais']

    def setUp(self):
        self.programa = Programa.objects.get(pk=1)

    def test_fixtures_data(self):
        """Teste para verificar a quantidade de programas iniciais."""
        self.assertEqual(Programa.objects.count(), 9)

    def test_fixtures_data_programa(self):
        """Teste para verificar o título do primeiro programa."""
        self.assertEqual(self.programa.titulo, 'Coisas bizarras')

    def test_fixtures_data_programa_likes(self):
        """Teste para verificar a quantidade de likes do primeiro programa."""
        self.assertEqual(self.programa.likes, 7864)
