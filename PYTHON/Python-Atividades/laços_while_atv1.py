# INGREDIENTES PARA UMA PIZZA
ingredientes = "\nQuais ingredientes irá querer para sua pizza?"
ingredientes += "\nDigite 'q' para finalizar seu pedido. "

while True:
    ingrediente = input(ingredientes)

    if ingrediente == 'q':
        break
    else:
        print("\nAdicionando " + ingrediente + " em sua pizza.")

# INGRESSOS PARA O CINEMA
mensagem = input("\nOlá. Quantos anos você tem? ")
mensagem = int(mensagem)

while True:

    if mensagem == 'q':
        break
    elif mensagem < 4:
        print("Seu ingreço é gratuíto. Bom filme.")
        break
    elif mensagem < 13:
        print("Seu ingreço custa $10. Bom filme.")
        break
    elif mensagem >= 13:
        print("Seu ingreço custa $15. Bom filme.")
        break

# TRÊS SAÍDAS
ingredientes = "\nQuais ingredientes irá querer para sua pizza?"
ingredientes += "\nDigite 'q' para encerrar sua lista de ingredientes. "

    # Laço while simples
ingrediente = ""
while ingrediente != 'q':
    ingrediente = input(ingredientes)

    if ingrediente != 'q':
        print("\nDicionando " + ingrediente + " na sua pizza.")
    
    # Uma flag
active = True
while active:
    ingrediente = input(ingredientes)
    
    if ingrediente == 'q':
        active = False
    else:
        print("\nAdicionando " + ingrediente + " na sua pizza.")

    # Instrução break
while True:
    ingrediente = input(ingredientes)

    if ingrediente == 'q':
        break
    else:
        print("\nAdicionando " + ingrediente + " na sua pizza.")