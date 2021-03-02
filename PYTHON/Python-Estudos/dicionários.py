alien_0 = {'color': 'green', 'points': 5}

# UM DICIONÁRIO SIMPLES
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

# ADICIONANDO NOVOS PARES chave-valor
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# COMEÇANO COM UM DICIONÁRIO VAZIO
alien_0 = {'color': 'green', 'points': 5}

print(alien_0)

# MODIFICANDO VALORES EM UM DICIONÁRIO
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

# MONITORANDO A POSIÇÃO DE UM ALIENIGENA
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'fast'}
print("Original x_position: " + str(alien_0['x_position']))

# Move o alienigena para a direita
# Determina a distancia que o alienigena deve se deslocar de acordo com
# sua velocidade atual
if alien_0['speed'] == 'slow':
    x_icrement = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # Este deve ser um alienigena rápido
    x_increment = 3

# A nova posição é a posição antiga somada ao incremento
alien_0['x_position'] += x_increment

print("New x-position: " + str(alien_0['x_position']))

# Removendo pares chave-valor
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

# Um dicionário de objetos semelhantes
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
        language.title() + ".")