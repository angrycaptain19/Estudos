### Verificando se é o usuário correto
import json
nome_arquivo = 'ARQUIVOS_JSON/alberto.json'


def chamar_nome_usuario():
    """Obtém o nome do usuário ja armazenado se estiver disponível."""
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
    with open(nome_arquivo, 'w') as objeto_arquivo:
        json.dump(nome_usuario, objeto_arquivo)
    return nome_usuario


def checar_usuario():
    """Verifica se o arquivo está correto."""
    """Caso não tenha nenhum arquivo relacinado, o programa vai 
    perguntar se quer registrar um novo usuário."""

    prompt = "\nARQUIVO NÃO ENCONTRADO!"
    prompt += "\nO arquivo pode não exitir ou o diretório está errado."
    prompt += "\nResponda com 'sim' ou 'não' se deseja registrar um novo usuário: "
    resposta = input(prompt)

    if resposta == 'sim':
        obter_novo_usuario()
        print("\nUSUÁRIO REGISTRADO!")
    elif resposta == 'não':
        try:
            with open(nome_arquivo) as objeto_arquivo:
                nome_usuario = json.load(objeto_arquivo)
        except FileNotFoundError:
            print("\nOPERAÇÃO CANCELADA!")
        else:
            return nome_usuario


def cumprimentar():
    """Saúda o usuário pelo nome."""
    nome_usuario = chamar_nome_usuario()
    if nome_usuario:
        print("\nBem vindo(a) devolta, " + nome_usuario.title() + "!")
    else:
        nome_usuario = checar_usuario()


cumprimentar()
