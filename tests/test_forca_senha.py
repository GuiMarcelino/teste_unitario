from unittest import TestCase

from forca_senha import numero_de_caracteres , letras_maiusculas, letras_minusculas

class TestForcaSenha(TestCase):
    def test_numero_de_caracteres(self):
        resultado = numero_de_caracteres("CeciliA160221")
        self.assertEqual(resultado, 52)

    def test_letras_maiusculas(self):
        resultado = letras_maiusculas("CeciliA160221")
        self.assertEqual(resultado, 22) # tamanho da string - letras maiusculas vezes 2

    def test_letras_minusculas(self):
        resultado = letras_minusculas("CeciliA160221")
        self.assertEqual(resultado, 10) # tamanho da string - letras minusculas vezes 2