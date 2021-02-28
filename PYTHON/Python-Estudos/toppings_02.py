# VERIFICANDO ITENS ESPECIAIS EM UMA LISTA
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out off green peppers right now.")
    else:
        print("adding " + requested_topping + ".")

print("\nFinished making your pizza!")

# VERIFICANDO SE UMA LISTA NÃO ESTÁ VAZIA.
requested_toppings = [] # listas vazias devolvem False

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")  # o bloco é acionado caso a lista devolva True. Ou seja,
    print("\nFinished making your pizza!")          # a lista deverá ter, pelo menos, um item.
else:
    print("\nAre you sure you want a plain pizza?")