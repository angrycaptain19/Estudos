bicycles = ['trek', 'cannondale', 'redline', 'specialized']

# INTRODUÇÃO ÀS LISTAS
print(bicycles)

# ACESSANDO ELEMENTOS INDIVIDUAIS DE UMA LISTA
print(bicycles[0].title())

# A POSIÇÃO DOS ÍNDICES COMEÇAM EM 0, E NÃO EM 1
print(bicycles[1].title())
print(bicycles[3].title())

# DEVOLVENDO O ÚLTIMO ITEM DA LISTA
print(bicycles[-1].title())

# USANDO VALORES INDIVIDUAIS DE UMA LISTA
message = "My first bicycle was a " + bicycles[0].title() + "."

print(message)