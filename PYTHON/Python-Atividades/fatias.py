comidas = ['pizza', 'hamburguer', 'macarrão', 'frango assado', 'linguiça']
print(comidas)

###
print("\nAs três primeiras comida da lista são:")
print(comidas[:3])

print("\nAs comidas do meio são:")
print(comidas[1:4])

print("\nAs três ultimas comidas da lista são:")
print(comidas[-3:])

###
minhas_pizzas = ['calabresa', 'queijo', 'bacon', 'carne seca']
pizzas_amigos = minhas_pizzas[:]

minhas_pizzas.append('churrasco')
pizzas_amigos.append('portuguesa')

print("\nMinhas pizzas favoritas são:")
for pizza in minhas_pizzas:
    print(pizza.title())

print('\nAs pizzas favoritas dos meus amigos são:')
for pizza in pizzas_amigos:
    print(pizza.title())