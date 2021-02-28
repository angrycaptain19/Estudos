# CRIANDO E USANDO UMA CLASSE
class Cachorro():
    """Uma tentativa simples de modelar um cachorro."""

    def __init__(self, nome, idade):
        """Inicializa os atributos nome e idade."""
        self.nome = nome
        self.idade = idade

    def sentar(self):
        """Simula um cachorro sentando em resposta a um comando."""
        print(self.nome.title() + " está sentando agora.")

    def rolar(self):
        """Simula um cachorro rolando em resposta a um comando."""
        print(self.nome.title() + " está rolando.")

# CRIANDO INSTÂNCIAS, ACESSANDO ATRIBUTOS E CHAMANDO MÉTODOS
# A PARTIR DE UMA CLASSE
meu_cachorro = Cachorro(nome='simba', idade=2)
seu_cachorro = Cachorro(nome='mylom', idade=8)

print("Meu cachorro se chama " + meu_cachorro.nome.title() + ".")
print("Meu cachorro tem " + str(meu_cachorro.idade) + " anos de idade.")
meu_cachorro.sentar()
meu_cachorro.rolar()

print("\nSeu cachorro se chama " + seu_cachorro.nome.title() + ".")
print("Seu cachorro tem " + str(seu_cachorro.idade) + " anos de idade.")
seu_cachorro.sentar()
seu_cachorro.rolar()