# TRABALHANDO COM CLASSES E INSTÂNCIAS
class Carro():
    """Uma tentativa simples de representar um carro."""

    def __init__(self, fabricante, modelo, ano):
        """Inicializa os atributos que descrevem um carro."""
        self.fabricante = fabricante
        self.modelo = modelo
        self.ano = ano


    def nome_descritivo(self):
        """Devolve um nome descritivo, formatado de modo elegante."""
        nome_carro = str(self.ano) + " " + self.fabricante + " " + self.modelo
        return nome_carro.title()


meu_novo_carro = Carro(fabricante='audi', modelo='a4', ano=2016)
print(meu_novo_carro.nome_descritivo())