convidados = ['samara', 'maria', 'lucas']

### LISTAS DE CONVIDADOS
print("Olá, " + convidados[0].title() + ". Você está convidado(a) para um encontro entre amigos")
print("Olá, " + convidados[1].title() + ". Você está convidado(a) para um encontro entre amigos")
print("Olá, " + convidados[2].title() + ". Você está convidado(a) para um encontro entre amigos")

### ALTERANDO A LISTA DE CONVIDADOS
print("\nInfelizmente, o(a) convidado(a) " + convidados[1].title() + " não poderá comparecer ao encontro")

convidados[1] = 'lorena'
print("\nOlá, " + convidados[0].title() + ". Você está convidado(a) para um encontro entre amigos")
print("Olá, " + convidados[1].title() + ". Você está convidado(a) para um encontro entre amigos")
print("Olá, " + convidados[2].title() + ". Você está convidado(a) para um encontro entre amigos")

### MAIS CONVIDADOS
print("\nOlá. achamos uma mesa maior como havia solicitado. Gostaria de adicionar mais alguém para o encontro?")

convidados.insert(0, 'elvis')
convidados.insert(2, 'maria')
convidados.append('bot')

print("\nOlá, " + convidados[0].title() + ". Você está convidado(a) para um encontro entre amigos")
print("Olá, " + convidados[1].title() + ". Você está convidado(a) para um encontro entre amigos")
print("Olá, " + convidados[2].title() + ". Você está convidado(a) para um encontro entre amigos")
print("Olá, " + convidados[3].title() + ". Você está convidado(a) para um encontro entre amigos")
print("Olá, " + convidados[4].title() + ". Você está convidado(a) para um encontro entre amigos")
print("Olá, " + convidados[5].title() + ". Você está convidado(a) para um encontro entre amigos")

### MOSTRANDO O NÚMERO DE CONVIDADOS
len(convidados)

### REDUZINDO A LISTA DE CONVIDADOS
print("\nPor motivos de segurança devido a alta de casos pelo Vírus, sua lista foi reduzida para dois convidados.")

removidos = convidados.pop(5)
print("\nOlá, " + removidos.title() + ". Venho avisar de antemão que, por motivos de segurança, o encontro terá de ser adiado."
"\nAgradeço a compreenção e espero lhe ver logo mais. abraços de seu amigo. Alberto.")

removidos = convidados.pop(4)
print("Olá, " + removidos.title() + ". Venho avisar de antemão que, por motivos de segurança, o encontro terá de ser adiado."
"\nAgradeço a compreenção e espero lhe ver logo mais. abraços de seu amigo. Alberto.")

removidos = convidados.pop(1)
print("Olá, " + removidos.title() + ". Venho avisar de antemão que, por motivos de segurança, o encontro terá de ser adiado."
"\nAgradeço a compreenção e espero lhe ver logo mais. abraços de seu amigo. Alberto.")

removidos = convidados.pop(0)
print("Olá, " + removidos.title() + ". Venho avisar de antemão que, por motivos de segurança, o encontro terá de ser adiado."
"\nAgradeço a compreenção e espero lhe ver logo mais. abraços de seu amigo. Alberto.")

print(convidados)
del convidados[1]
del convidados[0]

print(convidados)