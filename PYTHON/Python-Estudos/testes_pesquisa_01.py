import unittest
from pesquisa import PesquisaAnonima

class TestePesquisaAnonima(unittest.TestCase):
    """Testes para a classe PesquisaAnonima."""

    def setUp(self):
        """Cria uma pesquisa e um conjunto de respostas que poderão ser
        usados em todos os métodos de teste."""
        pergunta = "Qual foi a primeira língua que você aprendeu a falar?"
        self.minha_pesquisa = PesquisaAnonima(
            pergunta=pergunta
        )
        self.respostas = [
            'Inglês', 'Português', 'Francês'
        ]


    def test_resposta_unica(self):
        """Testa se uma única resposta é armazenada de 
        forma apropriada."""
        self.minha_pesquisa.conjunto_respostas(
            nova_resposta=self.respostas[0])
        self.assertIn(self.respostas[0], self.minha_pesquisa.respostas)

        
    def test_tres_respostas(self):
        """Testa se três respostas individuáis são armazenadas de 
        forma apropriada."""
        for resposta in self.respostas:
            self.minha_pesquisa.conjunto_respostas(
                nova_resposta=resposta
            )
        for resposta in self.respostas:
            self.assertIn(resposta, self.minha_pesquisa.respostas)


unittest.main()