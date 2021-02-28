# ORDENANDO UMA LISTA DE FORMA PERMANENTE COM O MÉTODO sort()
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# ORDENANDO UMA LISTA EM ORDEM ALFABÉTICA INVERSA
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

# ORDENANDO UMA LISTA TEMPORARIAMENTE COM O MÉTODO sorted()
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

# EXIBINDO UMA LISTA EM ORDEM INVERSA
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()  # o método reverse() muda a ordem da lista permanentemente
print(cars)     # basta usar o método um segunda vez restaurar a ordem.

# DESCOBRINDO O TAMANHO DE UMA LISTA
cars = ['bmw', 'audi', 'toyota', 'subaru'] # rodar no IDLE do python
len(cars)