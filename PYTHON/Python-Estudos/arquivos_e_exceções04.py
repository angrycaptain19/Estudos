import json
filename = 'ARQUIVOS_JSON/numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)


###
import json

nome_usuario = input("\nQual o seu nome? ")

nome_arquivo = 'ARQUIVOS_JSON/nome_usuário.json'
with open(nome_arquivo, 'w') as objeto_arquivo:
    json.dump(nome_usuario, objeto_arquivo)
    print("Vou me lembrar de você " + nome_usuario.title() + "!")

# Simulando uma entranda no app depois de um tempo.
import json

nome_arquivo = 'ARQUIVOS_JSON/nome_usuário.json'

with open(nome_arquivo) as objeto_arquivo:
    nome_usuario = json.load(objeto_arquivo)
    print("\nBem vindo(a) devolta, " + nome_usuario.title() + "!")


###
# Aprimorando o arquivo
import json

# Carrega o nome do usuário se foi armazenado anteriormente.
# Caso contrário, pede que o usuário forneça o nome e armazena essa
#  informção.
nome_arquivo = 'ARQUIVOS_JSON/samara.json'

try:
    with open(nome_arquivo) as objeto_arquivo:
        nome_usuario = json.load(objeto_arquivo)
except FileNotFoundError:
    nome_usuario = input("\nQual o seu nome? ")
    with open(nome_arquivo, 'w') as objeto_arquivo:
        json.dump(nome_usuario, objeto_arquivo)
        print("Vou me lembrar de você, " + nome_usuario.title() + ".")
else:
    print("Bem vindo(a) devolta, " + nome_usuario.title() + "!")

###

# Refatoração
import json

def chamar_nome_usuario():
    """Obtém o nome do usuário ja armazenado se estiver disponivel."""
    nome_arquivo = 'ARQUIVOS_JSON/bot_03.json'
    try:
        with open(nome_arquivo) as objeto_arquivo:
            nome_usuario = json.load(objeto_arquivo)
    except FileNotFoundError:
        return None
    else:
        return nome_usuario


def obter_novo_usuario():
    """Pede um novo nome de usuário."""
    nome_usuario = input("\nQual o seu nome? ")
    nome_arquivo = "ARQUIVOS_JSON/bot_03.json"
    with open(nome_arquivo, 'w') as objeto_arquivo:
        json.dump(nome_usuario, objeto_arquivo)
    return nome_usuario


def cumprimentar():
    """Saúda o usuário pelo nome."""
    nome_usuario = chamar_nome_usuario()
    if nome_usuario:
        print("Bem vindo(a) devolta, " + nome_usuario.title() + "!")
    else:
        nome_usuario = obter_novo_usuario()
        print("Vou me lembrar de você, " + nome_usuario.title() + ".")


cumprimentar()