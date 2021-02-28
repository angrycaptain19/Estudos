# LACHONETE
sanduiches_pedidos = ['atum', 'salsicha', 'filé']
sanduiches_prontos = []

while sanduiches_pedidos:
    sanduiche_atual = sanduiches_pedidos.pop()

    print("\nVerificando o seu sanduiche de " + sanduiche_atual + ".")
    sanduiches_prontos.append(sanduiche_atual)

print("\nOs sanduiches prontos são:")
for sanduiche_pronto in sanduiches_prontos:
    print("Sanduiche de " + sanduiche_pronto)

# SEM PASTRAMI
sanduiches_pedidos = [
    'pastrami', 'atum', 'pastrami', 'salsicha', 'pastrami', 'filé'
    ]
sanduiches_prontos = []

while 'pastrami' in sanduiches_pedidos:
    sanduiches_pedidos.remove('pastrami')

while sanduiches_pedidos:
    sanduiche_atual = sanduiches_pedidos.pop()

    print("\nVerificando o seu sanduiche de " + sanduiche_atual + ".")
    sanduiches_prontos.append(sanduiche_atual)

print("\nOs sanduiches prontos são:")
for sanduiche_pronto in sanduiches_prontos:
    print("Sanduiche de " + sanduiche_pronto)

# FÉRIAS DOS SONHOS
respostas = {}

enquete = True

while enquete:
    nome = input("\nQual o seu nome? ")
    resposta = input("Se pudesse visitar um lugar no mundo, para onde você iria? ")

    respostas[nome] = resposta

    repetir = input("Mais alguém gostaria de participar da enquete? (sim / nao) ")
    if repetir == 'nao':
        enquete = False

print("\n--- Resultados da enquete ---")
for nome, resposta in respostas.items():
    print(nome.title() + " gostaria de viajar para o(a) " + resposta.title() + ".")