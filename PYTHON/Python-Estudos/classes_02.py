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
        Rejeita a alteração se for tentativa de definir um valor menor
        para o hodômetro.
        """
        if quilometragem >= self.leitura_hodometro:
            self.leitura_hodometro = quilometragem
        else:
            print("Não pode fornecer uma quilometragem menor que a atual!")


meu_novo_carro = Carro(fabricante='audi', modelo='a4', ano=2016)
print(meu_novo_carro.nome_descritivo())

# Modificando o valor de um atributo diretamente
meu_novo_carro.leitura_hodometro = 23
meu_novo_carro.ler_hodometro()

# Modificando o valor de um atributo com um método
meu_novo_carro.atualizar_hodometro(quilometragem=24)
meu_novo_carro.ler_hodometro()