# TESTES CONDICIONAIS

# animais
animal = 'cachorro'
print("Se o animal == 'gato'? Eu digo que é False.")
print(animal == 'gato')

print("\nSe o animal == 'cachorro'? Eu digo que é True.")
print(animal == 'cachorro')

# carros
carro = 'fiat'
print("\nSe o carro == 'fiat'? Eu digo que é True.")
print(carro == 'fiat')

print("\nSe o carro == 'chevrolet'? Eu digo que é False.")
print(carro == 'chevrolet')

# comidas
comida = 'pizza'
print("\nSe a comida == 'hamburguer'? Eu digo que é False.")
print(comida == 'hamburguer')

print("\nSe a comida == 'pizza'? Eu digo que é True.")
print(comida == 'pizza')

# notebooks
notebook = 'lenovo'
print("\nSe o notebok for == 'lenovo'? Eu digo que é True.")
print(notebook == 'lenovo')

print("\nSe o notebook for == 'sansung'? Eu digo que é False.")
print(notebook == 'sansung')

# smartphones
smartphone = 'nokia'
print("\nSe o smartphone for == 'lenovo'? Eu digo que é False.")
print(smartphone == 'lenovo')

print("\nSe o smartphone for == 'nokia'? Eu digo que é True.")
print(smartphone == 'nokia')

###
# respostas
resposta = 'b'

if resposta != 'a':
    print("\nA resposta está errada. Por favor tente novamente.")
    
print(resposta != 'a')

resposta = 'a'
if resposta == 'a':
    print("Resposta correta!")

print(resposta != 'a')

# desconsiderando letras maiúsculas
nome = 'Alberto'

print("\nO nome " + nome + " é == a 'alberto'?")
print(nome == 'alberto')    # False

print("\nUsando o método 'lower()' podemos assemelhar a variável com o valor de interesse?")
print(nome.lower() == 'alberto')    # True

# números
idade = 18

print("\nComparando minha idade com dos meus amigos:")

print(idade == 18)  # True
print(idade != 19)  # True
print(idade > 10)   # True
print(idade < 27)   # True
print(idade >= 19)  # False
print(idade <= 18)  # True

# 'and' e 'or'
idade_0 = 18
idade_1 = 15

print("\nVerificando se as idades são aceitaveis:")
print((idade_0 >= 19) and (idade_1 >= 19))  # False
print((idade_0 <= 20) and (idade_1 <= 20))  # True
print((idade_0 >= 19) or (idade_1 >= 19))   # False
print((idade_0 <= 17) or (idade_1 <= 17))   # True 

# Verificando se um valor está em uma lista
favoritos = ['alan', 'cellbit', 'felps', 'saiko']

print("\nVerificando se streamers estão na lista:")
print('calango' in favoritos)   # False
print('alan' in favoritos)  # True

# Verificando se um valor não está em uma lista
favoritos = ['alan', 'cellbit', 'felps', 'saiko']

streamer = 'calango'
if streamer not in favoritos:
    print("\nOlá " + streamer.title() + ". Infelizmente você não se encontra na lista.")
    # True