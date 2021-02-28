from pesquisa import PesquisaAnonima

# Define uma pergunta e cria uma pesquisa
pergunta = ("Qual foi a primeira língua que você aprendeu a falar?")
minha_pesquisa = PesquisaAnonima(
    pergunta=pergunta
)


# Mostra a pergunta e armazena as respostas à pergunta
minha_pesquisa.mostrar_pergunta()
print("Tecle 's' + ENTER para sair.\n")
while True:
    resposta = input("Língua: ")
    if resposta == 's':
        break
    minha_pesquisa.conjunto_respostas(
        nova_resposta=resposta
    )


# Exibe os resultados da pesquisa
print("\nObrigado a todos por participarem da minha pesquisa!")
minha_pesquisa.mostrar_resultados()