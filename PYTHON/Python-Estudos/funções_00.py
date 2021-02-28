# PASSANDO INFORMAÇÕES PARA UMA FUNÇÃO
def greet_user(username):
    """Exibe saudação simples"""
    print("Hello, " + username.title() + "!")

greet_user('alberto')

# ARGUMENTOS POSICIONAIS e VÁRIAS CHAMADAS DE FUNÇÃO

def describe_pet(animal_type, pet_name):
    """Exibe informações sobre um animal de estimação."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
describe_pet('bot', 'lontra')   # A ordem é importante em argumentos posicionais

# ARGUMENTOS NOMEADOS ou KEYWORD ARGUMENTS
def descrição_pessoa(nome, ano):
    """Exibe o nome da pessoa e o ano de nascimento"""
    print("\nNome: " + nome.title())
    print("Ano de nascimento: " + str(ano))

descrição_pessoa(nome='alberto', ano=2000)

# VALORES DEFAULT
def informação_pessoa(nome, país='brasil'):
    """Exibe o nome da pessoa e o país onde ela mora atualmente"""
    print("\nNome: " + nome.title())
    print(nome.title() + " mora no(a) " + país.title() + ".")

informação_pessoa(nome='alberto')
informação_pessoa(país='canadá', nome='samara')

# CHAMADAS DE FUNÇÃO EQUIVALENTES
def cor_favorita(nome, cor='preta'):

    # Uma pessoa que gosta da cor preta
    cor_favorita('alberto')
    cor_favorita(nome='alberto')

    # Uma pessoa que gosta da cor azul
    cor_favorita('samara', 'azul')
    cor_favorita(nome='samara', cor='azul')
    cor_favorita(cor='azul', nome='samara')