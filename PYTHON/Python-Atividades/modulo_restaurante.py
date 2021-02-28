"""Uma classe que pode ser usada para representar um restaurante."""

class Restaurante():
    """Uma tentativa simples de modelar um restaurante."""

    def __init__(self, nome_restaurante, tipo_cozinha):
        """Inicializa os atributos do método."""
        self.nome_restaurante = nome_restaurante
        self.tipo_cozinha = tipo_cozinha
        self.pessoas_atendidas = 0

    
    def descrição_restaurante(self):
        """
        Descreve o restaurante usando os atributos
        da classe Restaurante.
        """
        print("Restaurante: " + self.nome_restaurante.title())
        print("Tipo de cozinha: " + self.tipo_cozinha.title())


    def restaurante_aberto(self):
        """Exibe uma mensagem dizendo que o restaurante está aberto."""
        print("O restaurante " + self.nome_restaurante.title() +
            " está aberto.")


    def definir_pessoas_atendidas(self, numero):
        """
        Nos permite definir o número de clientes atendidos.
        Regeita a alteração se a tentativa de definir um valor for
        menor para o número de pessoas atendidas.
        """
        if numero >= self.pessoas_atendidas:
            self.pessoas_atendidas = numero
        else:
            print("Não pode fornecer um número menor que o atual!")


    def ver_pessoas_atendidas(self):
        """Exibe uma frase que mostra o número de pessoas atendidas."""
        if self.pessoas_atendidas <2:
            print("Hoje foi atendido apenas 1 pessoa.")
        else:
            print("Hoje foram atendidos um total de " +
                str(self.pessoas_atendidas) + " pessoas.")


    def incrementando_pessoas_atendidas(self, adicional_atendido):
        """Soma a quantidade especificada ao valor de pessoas atendidas."""
        self.pessoas_atendidas += adicional_atendido

