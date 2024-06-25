from django.test import TestCase
from aluraflix.models import Programa

class ProgramaModelTestCase(TestCase):
    def setUp(self):
        self.programa = Programa.objects.create(titulo='Filme de Teste', data_lancamento='2020-01-01')

    def test_verifica_atributos_programa(self):
        """Teste para verificar os atributos do programa com valores default."""
        self.assertEqual(self.programa.titulo, 'Filme de Teste')
        self.assertEqual(self.programa.data_lancamento, '2020-01-01')
        self.assertEqual(self.programa.tipo, 'F')
        self.assertEqual(self.programa.likes, 0)
        self.assertEqual(self.programa.dislikes, 0)
