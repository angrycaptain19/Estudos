# PESSOAS
peoples = {
    'first_name': 'ingrid',
    'last_name': 'samara',
    'age': 15,
    'city': 'afogados da ingazeira',
    }

print(peoples)

# NÚMEROS FAVORITOS
numeros_favoritos = {
    'samara': 7,
    'alberto': 7,
    'lucas': 2,
    'demetrios': 27,
    'paloma': 20,
    'bot': 10,
    }

for nome, numero in numeros_favoritos.items():
    print("\nNome: " + nome.title())
    print("Número favorito: " + str(numero))

# GLOSSÁRIO
glossário = {
    'print()': 'Exibe uma linha de código no interpretador.',
    'for': 'Laço que percorre qualquer estrutura.',
    'set()': 'Torna itens repetidos em itens únicos.',
    'sorted()': 'Organiza os itens em ordem alfabética.',
    'if-elif-else': 'Instrução que trabalha com dados booleanos.',
    'items()': 'Trabalha com todos os dados fornecidos.',
    'keys()': 'Trabalha apenas com as chaves de um dicionário.',
    'values()': 'Trabalha apenas com os valores de um dicionário.',
    'in': 'Significa dizer que um item está em uma variável.',
    'not in': 'Significa dizer que um item não está em uma variável.',
    }

for palavra, significado in glossário.items():
    print("\nPalavra: " + palavra)
    print("Significado: " + significado)

# RIOS
rios = {
    'nilo': 'egito',
    'amazonas': 'america do sul',
    'colorado': 'estados unidos',
    'yangtsé': 'china',   
    }

print("\nOs rios mencionados são:")
for rio in sorted(rios.keys()):
    print(rio.title())

print("\nOs locais mencionados são:")
for local in sorted(rios.values()):
    print(local.title())

for rio, local in rios.items():
    if rio == 'colorado':
        print("\nO rio " + rio.title() + " corre pelos(as) " +
        local.title() + ".")
    else:
        print("\nO rio " + rio.title() + " corre pelo(a) " +
        local.title() + ".")

# ENQUETES
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'joão': 'java',
    'weliton': 'java',
    }

for nome in sorted(favorite_languages.keys()):
    print("\nOlá, " + nome.title() + ", obrigado por participar da minha "
    "pesquisa.")

if 'samara' not in favorite_languages.keys():
    print("\nOlá, Samara. Gostaria de participar da minha pesquisa?")