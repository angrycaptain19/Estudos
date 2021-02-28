"""Um simulador de arremeço de dados."""

from random import randint

class Dado:
    """Modela um arremeço do dado."""

    def __init__(self):
        """Inicializa o atributo que se refere aos lados de um dado."""
        self.lados_dado = 6

    def rolar_dado(self):
        """Arremeça o dado e cai em um numero aleatório."""
        if self.lados_dado == 6:
            self.lados_dado = randint(1, 6)
        elif self.lados_dado == 10:
            self.lados_dado = randint(1, 10)
        elif self.lados_dado == 20:
            self.lados_dado = randint(1, 20)

    def mostrar_dado(self):
        """Mostra o lado que o seu dado caiu depois do arremeço."""
        print("\nO lado que caiu foi o número: " + str(self.lados_dado))


dado = Dado()

for arremeço in range(10):
    dado.lados_dado = 20
    dado.rolar_dado()
    dado.mostrar_dado()