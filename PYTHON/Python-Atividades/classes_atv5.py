class Carro():
    """Uma tentativa simples de representar um carro."""
    
    def __init__(self, fabricante, modelo, ano):
        """Inicializa os atributos que descrevem um carro."""
        self.fabricante = fabricante
        self.modelo = modelo
        self.ano = ano
        self.leitura_hodometro = 0


    def nome_descritivo(self):
        """Devolve um nome descritivo, formatado de forma elegante."""
        nome_carro = str(self.ano) + " " + self.fabricante + " " + self.modelo
        return nome_carro.title()


    def ler_hodometro(self):
        """Exibe uma frase que mostra a milhagem do carro."""
        print("Esse carro têm " + str(self.leitura_hodometro) +
            " quilômetros rodados.")


    def atualizar_hodometro(self, quilometragem):
        """
        Define o valor de leitura do hodômetro com valor especificado.
        Rejeita a alteração se a tentativa de definir um valor for
        menor para o hodômetro.
        """
        if quilometragem >= self.leitura_hodometro:
            self.leitura_hodometro = quilometragem
        else:
            print("Não pode fornecer uma quilometragem menor que a atual!")


    def incrementar_hodometro(self, quilometros):
        """Soma a quantidade especificada ao valor de leitura do hodômetro."""
        self.leitura_hodometro += quilometros

    
    def abastecer_gasolina(self):
        """Simula o abastecimento do tanque de gasolina de um carro."""
        print("Abastecendo o tanque de gasolina.")


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


meu_tesla = Carro_Elétrico(
        fabricante='tesla',
        modelo='model s',
        ano=2016
        )

print(meu_tesla.nome_descritivo())

meu_tesla.bateria.descrição_bateria()
meu_tesla.bateria.obter_alcance()

meu_tesla.bateria.upgrade_bateria()
meu_tesla.bateria.obter_alcance()