"""Um conjunto de classe que pode ser usados para 
representar carros elétricos."""

from modulo_carro import Carro

class Bateria():
    """
    Uma tentativa simples de modelar uma bateria para um carro elétrico.
    """

    def __init__(self, capacidade_bateria=70):
        """Inicializa os atributos da bateria."""
        self.capacidade_bateria = capacidade_bateria


    def descrição_bateria(self):
        """Exibe uma frase que descreve a capacidade da bateria."""
        print("Esse carro tem uma bateria com capacidade total de " +
            str(self.capacidade_bateria) + "-KWh.")


    def upgrade_bateria(self):
        """Atualiza a capacidade da bateria."""
        if self.capacidade_bateria < 85:
            self.capacidade_bateria = 85
            print("A bateria do seu carro teve um upgrade e agora " +
                "tem uma capacidade total de 85-KWh.")


    def obter_alcance(self):
        """Exibe uma frase sobre a distância que o carro é capaz de
    percorrer com essa bateria."""
        if self.capacidade_bateria == 70:
            range = 240
        elif self.capacidade_bateria == 85:
            range = 270

        mensagem = "Esse carro pode percorrer, aproximadamente, "
        mensagem += str(range) + " quilometros."
        print(mensagem)


class Carro_Elétrico(Carro):
    """Representa aspectos específicos de veículos elétricos."""

    
    def __init__(self, fabricante, modelo, ano):
        """
        Inicializa os atributos da classe-pai.
        Em seguida, inicializa os atributos específicos de um carro
        eletrico.
        """
        super().__init__(fabricante, modelo, ano)
        self.bateria = Bateria()