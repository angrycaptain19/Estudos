### PESSOAS
from collections import OrderedDict

pessoas = OrderedDict

pessoa_01 = {
    'first_name': 'ingride',
    'last_name': 'samara',
    'age': 15,
    'city': 'afogados da ingazeira',
    }

pessoa_02 = {
    'first_name': 'alberto',
    'last_name': 'emanuel',
    'age': 20,
    'city': 'afogados da ingazeira',
    }

pessoa_03 = {
    'first_name': 'maria',
    'last_name': 'josé',
    'age': 50,
    'city': 'afogados da ingazeira',
    }

pessoas = [pessoa_01, pessoa_02, pessoa_03]

for pessoa in pessoas:
    print(pessoa)

### ANIMAIS DE ESTIMAÇÃO
animais = OrderedDict

cliford = {
    'tipo': 'cachorro',
    'dono': 'maria josé',
    }

kiara = {
    'tipo': 'cachorro',
    'dono': 'maria josé',
    }

simba = {
    'tipo': 'cachorro',
    'dono': 'maria marta',
    }

claudinha = {
    'tipo': 'lontra',
    'dono': 'alberto emanuel',
    }

animais = [cliford, kiara, simba, claudinha]

for animal in animais:
    print(animal)

### LUGARES FAVORITOS
lugares_favoritos = OrderedDict

lugares_favoritos = {
    'samara': ['dúbia', 'canadá', 'paris'],
    'maria': ['petrolândia'],
    'mariana': [],
    'alberto': ['canadá', 'estados unidos', 'paris']
    }

for nome, lugares in lugares_favoritos.items():
    if len(lugares) < 2:
        print("\nOlá, " + nome.title() +
            ". A pesquisa mostra que seu lugar favorito é:")
    else:
        print("\nOlá, " + nome.title() +
            ". A pequisa mostra que seus lugares favoritos são:")
    for lugar in lugares:
        print("\t" + lugar.title())

### NÚMEROS FAVORITOS
numeros_favoritos = OrderedDict

numeros_favoritos = {
    'samara': [7, 15],
    'alberto': [7, 20],
    'lucas': [2, 18],
    'demétrios': [27],
    'paloma': [20],
    'bot': [2, 0, 21]
    }

for nome, numeros in numeros_favoritos.items():
    if len(numeros) < 2:
        print("\nO número favorito de " + nome.title() + " é:")
    else:
        print("\n Os números favoritos de " + nome.title() + " são:")
    for numero in numeros:
        print("\t" + str(numero))

### PAÍSES
países = OrderedDict

países = {
    'canada': {
        'localização': 'américa do norte',
        'população': '37.59 milhões',
        'curiosidade': 'Possui a maior fronteira terrestre do mundo.',
        },

    'brasil': {
        'localização': 'américa do sul',
        'população': '212.6 milhões',
        'curiosidade': 'Possui o maior reservatório de água doce do mundo.',
        },

    'china': {
        'localização': 'ásia oriental',
        'população': '1.398 bilhões',
        'curiosidade': 'Quase um quinto da população mundial se encontra na china.',
        },
    }

for país, dados in países.items():
    print("\nPaís: " + país.title())

    localização = dados['localização']
    população = dados['população']
    curiosidade = dados['curiosidade']

    print("\tLocalização: " + localização.title())
    print("\tPopulação: " + população)
    print("\tCuriosidade: " + curiosidade)