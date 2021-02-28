import unittest
from nome_função import obter_nome_completo

class NomeCasoTeste(unittest.TestCase):
    """Testes para 'nome_função.py'."""
    

    def test_nome_sobrenome(self):
        """Nomes como 'Alberto Mendes' funcionam?"""
        nome_formatado = obter_nome_completo(
            nome='alberto', sobrenome='mendes'
        )
        self.assertEqual(nome_formatado, 'Alberto Mendes')

    
    def test_nome_meio_sobrenome(self):
        """Nomes como 'Alberto Emanuel Mendes' funcionam?"""
        nome_formatado = obter_nome_completo(
            nome='alberto', meio='emanuel', sobrenome='mendes'
        )
        self.assertEqual(nome_formatado, 'Alberto Emanuel Mendes')


unittest.main()