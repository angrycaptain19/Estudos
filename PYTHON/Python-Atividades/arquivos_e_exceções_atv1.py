# Lendo um arquivo inteiro
nome_arquivo = 'ARQUIVOS_TEXTO/aprendendo_python.txt'

with open(nome_arquivo) as objeto_arquivo:
    conteudo = objeto_arquivo.read()
    print(conteudo.strip())

# Lendo dados linha a linha
nome_arquivo = 'ARQUIVOS_TEXTO/aprendendo_python.txt'

with open(nome_arquivo) as objeto_arquivo:
    for line in objeto_arquivo:
        print(line.strip())

# Criando uma lista de linhas de uma arquivo
nome_arquivo = 'ARQUIVOS_TEXTO/aprendendo_python.txt'

with open(nome_arquivo) as objeto_arquivo:
    lines = objeto_arquivo.readlines()

linhas_string = ''
for line in lines:
    linhas_string += line.strip()

print(linhas_string)

# Aprendendo C
nome_arquivo = 'ARQUIVOS_TEXTO/aprendendo_python.txt'

with open(nome_arquivo) as objeto_arquivo:
    for linha in objeto_arquivo:
        linha.replace('python', 'C') # Só funciona no terminal python.
        print(linha.strip())    