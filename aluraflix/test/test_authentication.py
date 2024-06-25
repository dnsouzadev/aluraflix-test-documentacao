from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse

class AuthenticationUserTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('programas-list')
        self.user = User.objects.create_user(username='teste', password='teste123')

    def test_autenticacao_user_com_credenciais_corretas(self):
        """Teste para verificar a autenticação do usuário."""
        user = authenticate(username='teste', password='teste123')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_requisicao_nao_autorizada(self):
        """Teste para verificar a requisição sem autenticar."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 401)

    def test_autenticacao_user_com_credenciais_erradas(self):
        """Teste para verificar a autenticação do usuário."""
        user = authenticate(username='teste', password='senha')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_requisicao_autorizada(self):
        """Teste para verificar a requisição autenticada."""
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
