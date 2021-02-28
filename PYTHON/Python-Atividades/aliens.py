# cores de alienigena_1
alien_color = 'green'

if alien_color == 'green':
    points = 5
elif alien_color == 'yellow':
    points = 10
elif alien_color == 'red':
    points = 15

print("Você acabou de ganhar " + str(points) + " pontos.")

# estágios da nossa vida
age = 11

if age < 2:
    print("Você é um bebê.")
elif age < 4:
    print("Você é uma criança.")
elif age < 13:
    print("Você é um(a) garoto(a).")
elif age < 20:
    print("Você é um(a) adolescente.")
elif age < 65:
    print("Você é um adulto.")
elif age >= 65:
    print("Você é um idoso.")

# fruta favorita
favorite_fruits = ['manga', 'ciriguela', 'pitomba', 'maçã verde', 'pêra']

if 'banana' in favorite_fruits:
    print("Você realmente gosta de bananas.")
if 'ciriguela' in favorite_fruits:
    print("Você realmente gosta de ciriguelas.")
if 'pitomba' in favorite_fruits:
    print("Você realmente gosta de pitombas.")
if 'caju' in favorite_fruits:
    print("Você realmente gosta de cajus.")
if 'maçã verde' in favorite_fruits:
    print("Você realmente gosta de maçã verde.")