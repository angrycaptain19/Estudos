# COMO A FUNÇÃO input() TRABALHA
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# ESCREVENDO prompts CLAROS
name = input("Please enter your name: ")
print("Hello, " + name.title() + "!")

###

prompt = "\nIf you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("\nHello, " + name.title() + "!")

# USANDO int() PARA ACEITAR ENTRADAS NUMÉRICAS
age = input("\nHow old are you? ")
print(age)  # Devolve a entrada no valor de uma string.

age = int(age)  # Transforma a entrada no valor numérico.
print(age >= 18)

###
height = input("\nHow tall are you, in inches? ")
height = int(height)

if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

# OPERADOR DE MÓDULO - %
print(4 % 3)
print(5 % 3)
print(6 % 3)
print(7 % 3)

###
number = input("\nEnter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")