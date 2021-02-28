import unittest

from funcionarios import Funcionario


class TesteFuncionario(unittest.TestCase):
    """Testes para a classe Funcionario."""

    def setUp(self):
        """Cria um conjunto de informações que podems ser usados
        em todos os métodos de teste."""
        self.alberto = Funcionario(
            nome='alberto',
            sobrenome='mendes',
            salario=50000
        )


    def test_receber_aumento_padrão(self):
        """Testa se o funcionário receberá 5000 ao valor anual."""
        self.alberto.receber_aumento()
        self.assertEqual(self.alberto.salario, 55000)


    def test_receber_aumento_personalizado(self):
        """Testa se o funcionário pode receber um valor maior ou menor
        que 5000."""
        self.alberto.receber_aumento(
            aumento=10000
        )
        self.assertEqual(self.alberto.salario, 60000)

unittest.main()