# EXCEÇÕES
# Tratando a exceção ZeroDivisionError
# Usando blocos try-except
try:
    print(5/0)
except ZeroDivisionError:
    print("Você não pode dividir por zero!")


# Usando exceções para evitar falhas
# Crinando uma calculadora que faça apenas divisões:
print("\nMe forneça dois números e eu vou fazer a divisão entre eles.")
print("Tecle 's' + Enter para sair.")

while True:
    primeiro_numero = input("\nPrimeiro numero: ")
    if primeiro_numero == 's':
        break
    segundo_numero = input("\nSegundo numero: ")
    if primeiro_numero == 's':
        break
    try:
        resposta = int(primeiro_numero) / int(segundo_numero)
    except ZeroDivisionError:
        print("Você não pode dividir um número por zero!")
    else:
        print(resposta)


# Tratando a exceção FileNotfoundError
# Passando o programa para uma função
# Analisando textos
def contando_palavras(nome_arquivo):
    """Conta o número aproximado de palavras em um arquivo."""
    try:
        with open(nome_arquivo) as arquivo_objeto:
            conteudo = arquivo_objeto.read()
    except FileNotFoundError:
        msg = ("\nO nome do argumento '" + nome_arquivo +
            " não existe ou se encontra em outro diretório.")
        print(msg)
        # 'pass' para o bloco falhar silenciosamente
    else:
        # Conta o número aproximado de palavras no arquivo
        palavras = conteudo.split()
        num_palavras = len(palavras)
        print("\nO argumendo '" + nome_arquivo +
            " têm, aproximadamente, "+ str(num_palavras) + " palavras.")


nomes_arquivos = [
    'ARQUIVOS_TEXTO/CURSO_EXTENSIVO_PYTHON/chapter_10/alice.txt',
    'ARQUIVOS_TEXTO/CURSO_EXTENSIVO_PYTHON/chapter_10/moby_dick.txt',
    'ARQUIVOS_TEXTO/siddhartha.txt',
    'ARQUIVOS_TEXTO/CURSO_EXTENSIVO_PYTHON/chapter_10/little_women.txt'
    ]
for arquivo in nomes_arquivos:
    contando_palavras(nome_arquivo=arquivo)