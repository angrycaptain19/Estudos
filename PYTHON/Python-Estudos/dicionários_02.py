# UMA LISTA DE DICIONÁRIOS
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens =[alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

###

# Cria uma lista vazia para criar armazenar alienigenas
aliens = []

new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
# Cria 30 alienigenas verdes
for _ in range(30):
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# Mostra os 5 primeiros alienigenas
for alien in aliens[:5]:
    print(alien)
print("...")

# Mostra quantos alienigenas foram criados
print("Total number of aliens: " + str(len(aliens)))

### UMA LISTA EM UM DICIONÁRIO
# Armazena uma informações sobre uma pizza que está sendo pedida
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

# Resume o pedido
print("\nYou ordered a " + pizza['crust'] + "-crust pizza " +
    "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)

### LIGUAGENS FAVORITAS
from collections import OrderedDict

favorite_languages = OrderedDict

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, languages in favorite_languages.items():
    if len(languages) < 2:
        print("\n" + name.title() + "'s fatorite language is:")
    else:
        print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())

### UM DICIONÁRIO EM UM DICIONÁRIO
users = {
    'aeinstenin': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        }
    }

for username, user_info in users.items():
    print("\nUsername: " + username)

    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())