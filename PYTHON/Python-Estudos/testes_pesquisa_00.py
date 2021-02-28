import unittest
from pesquisa import PesquisaAnonima

class TestePesquisaAnonima(unittest.TestCase):
    """Testes para a classe PesquisaAnonima"""

    def test_resposta_unica(self):
        """Testa se uma única resposta é armazenada de forma apropriada."""
        pergunta = "Qual a primeira língua que você aprendeu a falar?"
        minha_pesquisa = PesquisaAnonima(
            pergunta=pergunta
        )
        minha_pesquisa.conjunto_respostas(
            nova_resposta='Português'
        )

        self.assertIn('Português', minha_pesquisa.respostas)


    def test_tres_respostas(self):
        """Testa se três respostas individuais são armazenadas de
        forma apropriada."""
        pergunta = "Qual a primeira língua que você aprendeu a falar?"
        minha_pesquisa = PesquisaAnonima(
            pergunta=pergunta
        )

        respostas = [
            'Inglês', 'Português', 'Francês'
        ]
        for resposta in respostas:
            minha_pesquisa.conjunto_respostas(
                nova_resposta=resposta
            )

        for resposta in respostas:
            self.assertIn(resposta, minha_pesquisa.respostas)


unittest.main()