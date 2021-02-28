# RESTAURANTE
class Restaurante():
    """Uma tentativa simples de modelar um restaurante."""

    def __init__(self, nome_restaurante, tipo_cozinha):
        """Inicializa os atributos restaurante e cozinha."""
        self.nome_restaurante = nome_restaurante
        self.tipo_cozinha = tipo_cozinha


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

# Criando instâncias
restaurante_00 = Restaurante(
        nome_restaurante='bodega 1900',
        tipo_cozinha='rústica'
        )

restaurante_01 = Restaurante(
        nome_restaurante="lyle's",
        tipo_cozinha='inglesa'
        )

restaurante_02 = Restaurante(
        nome_restaurante='ristorante italia',
        tipo_cozinha='itálica'
        )

restaurante_03 = Restaurante(
        nome_restaurante='lasai',
        tipo_cozinha='brasileira'
        )

restaurante_04 = Restaurante(
        nome_restaurante='narcissa',
        tipo_cozinha='americano'
        )

# Acessando atributos e chamando métodos
print("Bem vindos ao restaurante " +
    restaurante_00.nome_restaurante.title() + ".")
print("O restaurante tem uma cozinha " +
    restaurante_00.tipo_cozinha + ".")

restaurante_00.restaurante_aberto()
restaurante_00.descrição_restaurante()
restaurante_01.descrição_restaurante()
restaurante_02.descrição_restaurante()
restaurante_03.descrição_restaurante()
restaurante_04.descrição_restaurante()


# CRIANDO UMA CLASSE PARA USUÁRIOS
class Usuário():
    """Modelar dados base de um usuário."""

    def __init__(self,
            nome, sobrenome, idade, sexo, escolaridade, origem
            ):
        """Inicializando os atributos para os parâmetros acima."""
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.sexo = sexo
        self.escolaridade = escolaridade
        self.origem = origem

        
    def apresentar(self):
        print("\nOlá, " + self.nome.title() + " " + self.sobrenome.title() +
            ". Bem vindo ao mundo da programação.")
    

    def descrição(self):
        print("\nAqui estão os dados que você nos forneceu até então:")
        print("Nome: " + self.nome.title())
        print("Sobrenome: " + self.sobrenome.title())
        print("Idade: " + str(self.idade))
        print("Sexo: " + self.sexo.title())
        print("Escolaridade: " + self.escolaridade.title())
        print("Origem: " + self.origem.title())



pessoa_00 = Usuário(
        nome='alberto', sobrenome='mendes', idade=20, sexo='masculino',
        escolaridade='médio completo', origem='brasileiro'
        )

pessoa_01 = Usuário(
        nome='samara', sobrenome='mendes', idade=15, sexo='feminino',
        escolaridade='fundamental completo', origem='brasileira'
        )

pessoa_02 = Usuário(
        nome='maria', sobrenome='mendes', idade=51, sexo='feminino',
        escolaridade='médio completo', origem='brasileira'
        )

pessoa_00.apresentar()
pessoa_00.descrição()

pessoa_01.apresentar()
pessoa_01.descrição()

pessoa_02.apresentar()
pessoa_02.descrição()