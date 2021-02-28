# SORVETERIA
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


class Sabores():
    """Modelar atributos e métodos relacionados a sabores de sorvete."""

    def __init__(self):
        """Conterá uma lista de sabores disponiveis."""
        self.lista_sabores = [
            'morango', 'coco', 'napolitano', 'amendoas', 'graviola',
            'maracujá', 'prestígio', 'mesclado', 'creme', 'flocos'
            ]


    def ver_lista(self):
        """Exibe uma lista de sabores disponíveis na sorveteria."""
        print("Os sabores disponíveis são:")
        for sabor in self.lista_sabores:
            print("\t" + sabor.title())


class Sorveteria(Restaurante):
    """Modelando uma Sorveria."""


    def __init__(self, nome_restaurante, tipo_cozinha):
        """
        Inicializa os atributos da classe-pai.
        Inicializa os atributos da classe Sorveteria.
        """
        super().__init__(nome_restaurante, tipo_cozinha)
        self.sabores = Sabores()


meu_sorvete = Sorveteria(
        nome_restaurante='sorveteria duas bolas',
        tipo_cozinha='fria'
        )

meu_sorvete.descrição_restaurante()
meu_sorvete.sabores.ver_lista()