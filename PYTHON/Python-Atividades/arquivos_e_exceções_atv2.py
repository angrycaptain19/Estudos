nome_arquivo = 'ARQUIVOS_TEXTO/convidados.txt'

pergunta = input("Qual o seu nome e sobrenome? ")

with open(nome_arquivo, 'a') as objeto_arquivo:
    objeto_arquivo.write(pergunta + "\n")