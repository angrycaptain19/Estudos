users = ['admin', 'alberto', 'samara', 'sabrina', 'lucas']

### sem usuários
if users:
    for user in users:
        if user == 'admin':
            print("Olá, Criador! Que bom que você está de volta.")
            print("Gostaria de ver o relatório de status de hoje?")
        else:
            print("Olá, " + user.title() + ". Obrigado por fazer login novamente.")
else:
    print("Precisamos encontrar novos usuários.")

### verificando nomes de usuários
current_users = ['alberto', 'samara', 'lucas', 'maria', 'jeferson']

new_users = ['MARIA', 'jorge', 'Lucas', 'joão', 'sabrina']

for new_user in new_users:
    if new_user.lower() in current_users:
        print("\nDesculpa. O nome " + new_user.title() + " já está sendo usado.")
    else:
        print("\nAdicinando " + new_user.title() + " a lista.")

print("\nLista finalizada!")

### números ordinais
numeros = list(range(1,10))

for numero in numeros:
    if numero == 1:
        print(str(numero) + "st")
    elif numero == 2:
        print(str(numero) + "nd")
    elif numero == 3:
        print(str(numero) + "rd")
    else:
        print(str(numero) + "th")

