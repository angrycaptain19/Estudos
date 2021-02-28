### contando até vinte
for numbers in range(1,21):
    print(numbers)

### Um milhão
#for numbers in range(1,1000001):
    #print(numbers)

### Somando um milhão
digits = range(1,1000001)
print(max(digits))
print(min(digits))
print(sum(digits))

### Números ímpares
impares = list(range(1,20,2))
print(impares)

### Três
três = list(range(3,31,3))
print(três)

### Cubos
cubos = []
for value in range(1,11):
    cubos.append(value**3)

print(cubos)

### Comprehension de cubos
cubos = [value**3 for value in range(1,11)]
print(cubos)