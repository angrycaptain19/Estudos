# ADMIN
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


class Privilégios():
    """Tudo relacionado a privilégios de um administrador é trabalhado
    nesta classe."""
    
    def __init__(self):
        """Inicia um atributo para a nossa lista de privilégios."""
        self.privilégios = [
            'alterar dados', 'administrar contas',
            'deletar contas', 'atualizar sistemas'
            ]


    def mostrar_privilégios(self):
        """Exibe os privilégios de ser um administrador."""
        print("Privilégios de um administrador:")
        for privilégio in self.privilégios:
            print("\t" + privilégio.title())


class Administrador(Usuário):
    """Modelando um ambiente específico com atributos adicionais
    para um administrador."""


    def __init__(self,
            nome, sobrenome, idade, sexo,
            escolaridade, origem
            ):
        """
        Inicializa os atributos da classe Usuário.
        Inicializa os atributos da classe Administrador.
        """
        super().__init__(
            nome, sobrenome, idade, sexo,
            escolaridade, origem
            )
        self.privilégios = Privilégios()

admin = Administrador(
        nome='alberto', sobrenome='mendes', idade=20, sexo='masculino',
        escolaridade='médio completo', origem='brasil'
        )

admin.descrição()
admin.privilégios.mostrar_privilégios()