nome_arquivo = 'ARQUIVOS_TEXTO/lista_de_convidados.txt'

pergunta = "Por favor, entre com seu nome e sobrenome:\n"
pergunta += "Tecle 's' + ENTER para finalizar a pesquisa: \n"

while True:
    convidado = input(pergunta)
    if convidado == 's':
        break
    else:
        print("\nOlá, " + convidado.title() + ". Seja muito bem vindo(a)!\n")
        with open(nome_arquivo, 'a') as objeto_arquivo:
            objeto_arquivo.write(convidado.title() + "\n")