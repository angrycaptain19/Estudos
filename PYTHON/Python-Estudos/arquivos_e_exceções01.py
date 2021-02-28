# ESCREVENDO UM ARQUIVO VAZIO
filename = 'ARQUIVOS_TEXTO/mensagem_simples.txt'

with open(filename, 'w') as file_object:
    file_object.write("Eu amo programação!\n")
    file_object.write("Sou entusiasta da programação!\n")


# CONCATENANDO DADOS EM UM ARQUIVO
filename = 'ARQUIVOS_TEXTO/mensagem_simples.txt'

with open(filename, 'a') as file_object:
    file_object.write("É uma profição de muita satisfação, onde "
        "aprendemos sobre tecnologia, lógica, métodos e padrões, "
        "criando e modelando dados. É um mundo infinito!\n")
    file_object.write("Quero seguir na carreira de Engenheiro de"
        "software!\n")