# SINTAXE if-elif-else
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65: # podemos omitir o a instrução 'else' por uma 'elif' para ficar mais conciso
    price = 5

print("Your admission cost in $" + str(price) + ".")