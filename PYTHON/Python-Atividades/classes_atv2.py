# TENTATIVAS DE LOGIN
class Usuário():
    """Modelar dados base de um usuário."""

    def __init__(self,
            nome, sobrenome, idade, sexo, escolaridade, origem
            ):
        """Inicializando os atributos do método."""
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.sexo = sexo
        self.escolaridade = escolaridade
        self.origem = origem
        self.login_tentativas = 0


    def apresentar(self):
        """Exibe o nome do usuário de forma estilizada."""
        print("\nOlá, " + self.nome.title() + " " + self.sobrenome.title() +
            ". Bem vindo ao mundo da programação.")


    def descrição(self):
        """Exibe os dados obtidos do usuário."""
        print("\nAqui estão os dados fornecidos até então:")
        print("Nome: " + self.nome.title())
        print("Sobrenome: " + self.sobrenome.title())
        print("Idade: " + str(self.idade))
        print("Sexo: " + self.sexo.title())
        print("Escolaridade: " + self.escolaridade.title())
        print("Origem: " + self.origem.title())


    def incrementando_login_tentativas(self, somar_login):
        """
        Soma a quantidade de logins ao valor atual de tentativas de
        login.
        """
        self.login_tentativas += somar_login

    
    def resetar_login_tentativas(self):
        """Reseta o número de logins a 0."""
        self.login_tentativas = 0

    def ver_login_tentativas(self):
        """Exibe o número de logins do dia."""
        print("Tentativas de login: " + str(self.login_tentativas))


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
pessoa_00.incrementando_login_tentativas(somar_login=3)
pessoa_00.incrementando_login_tentativas(somar_login=7)
pessoa_00.ver_login_tentativas()
pessoa_00.resetar_login_tentativas()
pessoa_00.ver_login_tentativas()

pessoa_01.apresentar()
pessoa_01.descrição()

pessoa_02.apresentar()
pessoa_02.descrição()