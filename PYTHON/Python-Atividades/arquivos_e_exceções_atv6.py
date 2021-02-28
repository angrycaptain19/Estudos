# Número favorito
import json

numero_favorito = input("Qual o seu número favorito? ")

nome_arquivo = 'ARQUIVOS_JSON/numero_favorito.json'
with open(nome_arquivo, 'w') as objeto_arquivo:
    json.dump(numero_favorito, objeto_arquivo)

# Abrindo o arquivo 'numero_favorito.json'
with open(nome_arquivo) as objeto_arquivo:
    numero = json.load(objeto_arquivo)
    print("Eu sei qual é o seu número favorito. É " + str(numero) + ".")


### Lembrando o número favorito
import json

nome_arquivo = 'ARQUIVOS_JSON/numero_favorito_1.json'
try:
    with open(nome_arquivo) as objeto_arquivo:
        numero = json.load(objeto_arquivo)
except FileNotFoundError:
    numero_favorito = input("Qual o seu número favorito? ")
    with open(nome_arquivo, 'w') as objeto_arquivo:
        json.dump(numero_favorito, objeto_arquivo)
        print("Vou gravar qual o seu número favorito.")
else:
    print("O seu número favorito é " + str(numero) + ".")