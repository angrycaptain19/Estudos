# PESSOAS ATENDIDAS
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


restaurante_00 = Restaurante(
        nome_restaurante='bodega 1900',
        tipo_cozinha='rústica'
        )

restaurante_01 = Restaurante(
        nome_restaurante="lyle's",
        tipo_cozinha='inglesa'
        )

restaurante_02 = Restaurante(
        nome_restaurante='lasai',
        tipo_cozinha='brasileira'
        )

restaurante_03 = Restaurante(
        nome_restaurante='ristorante italia',
        tipo_cozinha='itálica'
        )

restaurante_04 = Restaurante(
        nome_restaurante='narcissa',
        tipo_cozinha='americano'
        )


print("Bem vindos ao restaurante " +
    restaurante_00.nome_restaurante.title() + ".")
print("O restaurante tem uma cozinha " +
    restaurante_00.tipo_cozinha + ".")

restaurante_00.descrição_restaurante()
restaurante_00.restaurante_aberto()

restaurante_01.descrição_restaurante()
restaurante_01.definir_pessoas_atendidas(numero=7)
restaurante_01.definir_pessoas_atendidas(numero=6)
restaurante_01.ver_pessoas_atendidas()

restaurante_02.descrição_restaurante()
restaurante_02.definir_pessoas_atendidas(numero=7)
restaurante_02.incrementando_pessoas_atendidas(adicional_atendido=7)
restaurante_02.ver_pessoas_atendidas()

restaurante_03.descrição_restaurante()

restaurante_04.descrição_restaurante()