"""Classes que contem os privilégios de um 
administrador e sua representação."""

from modulo_user import Usuário

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