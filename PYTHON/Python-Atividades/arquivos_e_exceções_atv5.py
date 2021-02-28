# Adição
print("Me forneça dois números e farei a soma entre eles dois:")
print("Tecle 's' + Enter para sair da operação.")

while True:
    primeiro_numero = input("\nPrimeiro número: ")
    if primeiro_numero == 's':
        break
    segundo_numero = input("\nSegundo número: ")
    if segundo_numero == 's':
        break
    try:
        resposta = int(primeiro_numero) + int(segundo_numero)
    except ValueError:
        print("Você não pode somar letras com números!")
    else:
        print(resposta)


# Gatos e Cachorros
def exibir_animais(nome_arquivo):
    """Mostra os animais que contem em uma lista."""
    try:
        with open(nome_arquivo) as arquivo_objeto:
            conteudo = arquivo_objeto.read()
    except FileNotFoundError:
        #msg = ("\nO arquivo '" + nome_arquivo + "' não existe ou "
            #"se encontra em outro diretório.")
            pass
        #print(msg)
    else:
        print(conteudo)



nome_arquivos = [
    'ARQUIVOS_TEXTO/gatos.txt',
    'RQUIVOS_TEXTO/cachorros.txt',
    ]
for arquivo in nome_arquivos:
    exibir_animais(nome_arquivo=arquivo)


# Palavras comuns
def contando_palavras(nome_arquivo):
    """Exibe quantas vezes uma palavra se repete em um arquivo"""
    try:
        with open(nome_arquivo) as arquivo_objeto:
            conteudo = arquivo_objeto.read()
    except FileNotFoundError:
        msg = ("O arquivo '" + nome_arquivo + "' não existe os se " +
            "encontra em outro diretório.")
        print(msg)
    else:
        palavras = conteudo.lower().count('the')
        print(palavras)


lista_arquivos = [
    'ARQUIVOS_TEXTO/CURSO_EXTENSIVO_PYTHON/chapter_10/alice.txt',
    'ARQUIVOS_TEXTO/CURSO_EXTENSIVO_PYTHON/chapter_10/moby_dick.txt',
    'ARQUIVOS_TEXTO/siddhartha.txt',
    'ARQUIVOS_TEXTO/CURSO_EXTENSIVO_PYTHON/chapter_10/little_women.txt'
    ]
for arquivo in lista_arquivos:
    contando_palavras(nome_arquivo=arquivo)