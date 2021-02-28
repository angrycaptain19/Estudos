# FATIANDO UMA LISTA
players = ['charles', 'martina', 'michael', 'florence', 'eli']

print(players[0:3]) # exibe uma fatia da lista (os itens 1,2 e 3)
print(players[1:4]) # exibe uma fatia da lista (os itens 2,3 e 4)
print(players[:4])  # omitir o primeiro índice da fatia informa a python que começe com o primeiro item
print(players[0:])  # omitir o ultimo índice da fatia informa a python que termine com o ultimo item
print(players[-3:]) # informando os três ultimos players (muito usado para listas muito grandes ou que possam mudar constantemente de tamanho)

# PERCORRENDO UMA FATIA COM UM LAÇO
print("Here arede first three players on my team:")
for player in players[:3]:
    print(player.title())