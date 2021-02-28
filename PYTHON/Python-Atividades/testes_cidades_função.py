import unittest
from cidades_função import cidades

class CidadeCasoTeste(unittest.TestCase):
    """Testes para 'cidades_função.py'."""

    def test_cidade_país(self):
        """Saídas como 'Recife, Brasil' funcionam?"""
        conteudo = cidades(
            cidade='recife', 
            país='brasil'
        )
        self.assertEqual(conteudo, 'Recife, Brasil')


    def test_cidade_país_população(self):
        """Saídas como 'Recife, Brasil - população:' funcionam?"""
        conteudo = cidades(
            cidade='recife', 
            país='brasil', 
            população=1555000
        )
        self.assertEqual(conteudo, 
            "Recife, Brasil - População: 1555000 Habitantes.")


unittest.main()