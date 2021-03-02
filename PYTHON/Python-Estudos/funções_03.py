# PASSANDO UM NÚMERO ARBITRÁRIO DE ARGUMENTOS
def make_pizza(*toppings):
    """Apresenta a pizza que estamos prestes a preparar."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# MISTURANDO ARGUMENTOS POSICIONÁIS COM ARBITRÁRIOS
def fazer_pizza(size, *toppings):
    """Apresenta a pizza que estamos prestes a preparar."""
    print("\nMaking a " + str(size) +
        "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

fazer_pizza(16, 'pepperoni')
fazer_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# USANDO ARGUMENTOS NOMEADOS ARBITRÁRIOS
def build_profile(first, last, **user_info):
    """Constrói um dicionário contendo tudo o que sabemos sobre um usuário."""
    profile = {'first_name': first, 'last_name': last}
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile(
        first='albert', last='einstein',
        location='princeton', field='physics'
    )
print(user_profile)