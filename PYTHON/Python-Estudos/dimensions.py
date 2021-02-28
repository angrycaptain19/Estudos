# DEFININDO UMA TUPLA
dimensions = (200, 50)

print(dimensions[0])
print(dimensions[1])

# PERCORRENDO TODOS OS VALORES DE UMA TUPLA COM UM LAÇO
for dimension in dimensions:
    print(dimension)

# SOBRESCREVENDO UMA TUPLA
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModfield dimensions:")
for dimension in dimensions:
    print(dimension)