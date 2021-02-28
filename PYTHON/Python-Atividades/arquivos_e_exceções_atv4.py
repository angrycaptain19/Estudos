arquivo_texto = 'ARQUIVOS_TEXTO/enquete.txt'

pergunta = "\nPor que você gosta de programação?\n"
pergunta += "Tecle 's' + ENTER para sair da enquete.\n"

while True:
    resposta = input(pergunta)
    if resposta == 's':
        break
    else:
        with open(arquivo_texto, 'a') as objeto_arquivo:
            objeto_arquivo.write(resposta + "\n")