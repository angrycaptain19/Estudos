from testes_01 import obter_nome_completo

print("Tecle 's' + ENTER para sair.")
while True:
    nome = input("\nPor favor, me diga o seu primeiro nome: ")
    if nome == 's':
        break
    sobrenome = input("\nAgora me informe o seu sobrenome: ")
    if sobrenome == 's':
        break


    nome_formatado = obter_nome_completo(
            nome=nome, sobrenome=sobrenome
    )
    print("\tNome formatado: " + nome_formatado + ".")