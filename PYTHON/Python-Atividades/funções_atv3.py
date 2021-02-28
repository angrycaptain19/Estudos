# SANDUÍCHES
def sanduíche(*ingredientes):
    """Apresenta o sanduíche que estamos prestes a preparar."""
    print("\nIngredientes pedidos no sanduíche:")
    for ingrediente in ingredientes:
        print("- " + ingrediente)

sanduíche('salame', 'alface', 'colve')
sanduíche('presunto')
sanduíche('atum', 'carne moída', 'maionese')

# PERFIL DO USUÁRIO
def build_profile(first, last, **user_info):
    """Constrói um dicionário contendo tudo o que sabemos sobre o usuário."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile(
    first='alberto', last='mendes', age=20 , location='pernambuco', field='software engineer'
    )
print(user_profile)

# CARROS
def make_car(fabricante, modelo, **car_info):
    """Constrói um dicionário com informações sobre um carro."""
    profile = {}
    profile['fabricante'] = fabricante
    profile['modelo'] = modelo
    for key, value in car_info.items():
        profile[key] = value
    return profile

car_profile = make_car(
    fabricante='toyota', modelo='raize', ano_fabricado=2021, motor='turbo',
    tow_package=False
    )
print(car_profile)