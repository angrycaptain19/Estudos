# LAÇO WHILE
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# DEIXANDO O USUÁRIO DECIDIR QUANDO QUER SAIR
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)

# USANDO UMA flag
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

# USANDO break PARA SAIR DE UM LAÇO
prompt = "\nPlease enter the name of a city you have visted:"
prompt += "\nEnter to 'quit' when you are finished. "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")

# USANDO continue EM UM LAÇO
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    
    print(current_number)

# EVITANDO LOOPS INFINITOS
x = 1
while x <= 5 :
    print(x)
# Omitindo essa linha de código, o laço é execultado indefinidamente.    
    x += 1 
