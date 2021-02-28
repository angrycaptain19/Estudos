# VALORES DE RETORNO -- DEVOLVENDO UM VALOR SIMPLES
def get_formated_name(first_name, last_name):
    """Devolve um nome completo formatado de modo elegante."""
    full_name = first_name + " " + last_name
    return full_name.title()

musician = get_formated_name('jimi', 'hendrix')
print(musician)

# DEIXANDO UM ARGUMENTO OPCIONAL
def formatando_nome(first_name, last_name, middle_name=''):
    """Devolve um nome completo formatado de modo elegante."""
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()

musician = formatando_nome('jimi', 'hendrix')
print(musician)

musician = formatando_nome(first_name='john', last_name='hooker', middle_name='lee')
print(musician)

# DEVOLVENDO UM DICIONÁRIO
def build_person(first_name, last_name, age=''):
    """Devolve um dicionário com informáções de uma pessoa."""
    person = {
        'first': first_name, 'last': last_name,
    }
    if age:
        person['age'] = age
    return person

musician = build_person(last_name='hendrix', age=27, first_name='jimi')
print(musician)

# USANDO UMA FUNÇÃO COM UM LAÇO WHILE
def formatted_name(first_name, last_name):
    """Devolve um nome completo formatado de forma elegante."""
    full_name = first_name + " " + last_name
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    nome_formatado = formatted_name(f_name, l_name)
    print("\nHello, " + nome_formatado + "!")