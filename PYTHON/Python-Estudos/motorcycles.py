# ALTERANDO, ACRESCENTANDO E REMOVENDO ITENS DE UMA LISTA
motorcycles = ['honda', 'yamaha', 'suzuki']

# ALTERANDO UM ITEM DE UMA LISTA
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# ACRESCENTANDO ELEMENTOS EM UMA LISTA
# CONCATENANDO ELEMENTOS NO FINAL DE UMA LISTA
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

# ADICIONANDO ITENS A PARTIR DE UMA LISTA VAZIA
motorcycles = ['honda', 'yamaha', 'suzuki']

print(motorcycles)

# INSERINDO ELEMENTOS EM UMA LISTA
motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.insert(0, 'ducati')
print(motorcycles)

# REMOVENDO ELEMENTOS DE UMA LISTA
# instrução (del)
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[1]
print(motorcycles)

# método (pop)
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# utilizando em uma frase
motorcycles = ['honda', 'yamaha', 'suzuki']

last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

# REMOVENDO ITENS DE QUALQUER POSIÇÃO EM UMA LISTA
motorcycles = ['honda', 'yamaha', 'suzuki']

last_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a " + last_owned.title() + ".")

# REMOVENDO UM ITEM DE ACORDO COM O VALOR
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

# utilizando em uma frase
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'yamaha'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")