# TRANFERINDO ITENS DE UMA LISTA PARA OUTRA
# Começa com os usuários que precisam ser verificados,
# e com uma lista para armazenar os usários confirmados
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verifica cada usuário até que não haja mais usuários não confirmados
#   Transfere cada usuário verificado para a lista de usuários confirmados
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

# Exibe todos os usuários confirmados
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# REMOVENDO TODAS AS INSTÂNCIAS DE VALORES ESPECÍFICOS DE UMA LISTA
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

# PREENCHENDO UM DICIONÁRIO COM DADOS DE ENTRADA DE UM DICIONÁRIO
responses = {}

# Define uma flag para indicar que a enquete está ativa
polling_active = True

while polling_active:
    # Pede o nome da pessoa e a resposta
    name = input("\nWhat is your name? ")
    response = input("Whish mountain would you like to climb someday? ")

    # Armazena a resposta no dicionário
    responses[name] = response

    # Descobre se outra pessoa vai responder à enquete
    repeat = input("Would you like to let another person respond? (yes / no) ")
    if repeat == 'no':
        polling_active = False

# A enquete foi concluída. Mostra os resultados
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name.title() + " would you like climb " + response + ".")