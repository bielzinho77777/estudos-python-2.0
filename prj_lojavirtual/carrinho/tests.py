from django.test import TestCase

# Create your tests here.
from django.test import TestCase, RequestFactory
from django.contrib.sessions.middleware import SessionMiddleware
from .carrinho import Carrinho  # ajuste o caminho conforme necessário

class ProdutoFake:
    def __init__(self, id, preco):
        self.id = id
        self.preco = preco

class CarrinhoTestCase(TestCase):
    def setUp(self):
        # cria o request com sessão real
        self.factory = RequestFactory()
        self.request = self.factory.get('/')
        middleware = SessionMiddleware(lambda x: None)
        middleware.process_request(self.request)
        self.request.session.save()

        # cria instância do carrinho
        self.carrinho = Carrinho(self.request)

        # produto simulado
        self.produto = ProdutoFake(id=1, preco=10.00)

    def test_adicionar_produto(self):
        self.carrinho.adicionar(self.produto, quantidade=2)
        carrinho_data = self.request.session.get('carrinho')
        self.assertIsNotNone(carrinho_data)
        self.assertIn('1', carrinho_data)
        self.assertEqual(carrinho_data['1']['quantidade'], 2)
        self.assertEqual(carrinho_data['1']['preco'], '10.0')

    def test_limpar_carrinho(self):
        self.carrinho.adicionar(self.produto, quantidade=2)
        self.carrinho.limpar_carrinho()
        carrinho_data = self.request.session.get('carrinho')
        self.assertIsNone(carrinho_data)
