from django.test import TestCase
from aluraflix.models import Programa
from aluraflix.serializers import ProgramaSerializer

class ProgramaSerializerTestCase(TestCase):
    def setUp(self):
        self.programa = Programa.objects.create(
            titulo='Filme de Teste', data_lancamento='2020-01-01',
            likes=2340,
            dislikes=40
        )
        self.serializer = ProgramaSerializer(instance=self.programa)

    def test_verifica_campos_serializados(self):
        """Teste para verificar os campos serializados."""
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['titulo', 'tipo', 'data_lancamento', 'likes', 'dislikes']))

    def test_verifica_conteudo_campos_serializados(self):
        """Teste para verificar o conteúdo dos campos serializados."""
        data = self.serializer.data
        self.assertEqual(data['titulo'], self.programa.titulo)
        self.assertEqual(data['tipo'], self.programa.tipo)
        self.assertEqual(data['data_lancamento'], self.programa.data_lancamento)
        self.assertEqual(data['likes'], self.programa.likes)
        self.assertEqual(data['dislikes'], self.programa.dislikes)
