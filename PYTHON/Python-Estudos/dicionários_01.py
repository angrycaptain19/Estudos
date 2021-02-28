user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }

# PERCORRENDO TODOS OS PARES chave-valor COM UM LAÇO
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

# PERCORRENDO TODAS AS CHAVES DE UM DICIONÁRIO COM UM LAÇO
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

# Você pode omitir o método keys() pois o interpretador sabe que é um
# comportamento padrão percorrer as chaves.
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() +
        ", I see your favorite languages is " +
        favorite_languages[name].title() + "!")

# PERCORRENDO AS CHAVES DE UM DICIONÁRIO EM ORDEM USANDO UM LAÇO
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

# PERCORRENDO TODOS OS VALORES DE UM DICIONÁRIO COM UM LAÇO
print("\nThe following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())