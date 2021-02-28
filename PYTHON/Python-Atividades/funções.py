países = ['canada', 'estados unidos', 'frança', 'china', 'alemanha']

###
print("O " + países[0].title() + " é um dos países mais sofisticados do mundo!")

###
print("\nElimine um país que você não gostaria de conhecer:")
del países[-1]

print("Mostrando os países restantes da lista:")
print(países)

###
print("\nModifique a lista trocando um país por outro:")
países[-1] = 'espanha'

print("Mostrando a lista de países atualizada:")
print(países)

###
print("\nAcrescente um três países sendo um no começo, outro no meio e o outro no final da lista:")
países.insert(0, 'mexico')
países.insert(3, 'holanda')
países.insert(6, 'katar')   # ÍNDICE -1 COLOCARÁ O VALOR NA PENULTIMA POSIÇÃO

print("Mostrando a lista de países atualidada:")
print(países)

###
print("\nO dinheiro é insuficiente para todas as viagens e portando você deve remover um país da sua lista.")
países_descartados = países.pop(-1)

print("O país removido foi o(a) " + países_descartados.title() + ".")

###
print("\nRemova um país que não é sua prioridade no momento:")

não_prioridade = 'mexico'
países.remove(não_prioridade)

print("\n" + não_prioridade.title())
print("O(A) " + não_prioridade.title() + " não será prioridade no momento.")