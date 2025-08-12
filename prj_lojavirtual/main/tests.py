from django.test import TestCase
from django.urls import reverse
# Create your tests here.
class TestarPaginas(TestCase):
    def test_pagina_principal_OK(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, 'Minha Loja')
    
    def test_pagina_ajuda_carregacompleto(self):
        response = self.client.get(reverse("ajuda"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertContains(response, '<h3>1. Como comprar?</h3>')