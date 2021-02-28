pessoa = "alberto"

print("Olá, " + pessoa.title() + ". Gostaria de aprender Python hoje?") # APRESENTAÇÃO SIMPLES DE UMA VARIÁVEL
print("Olá, " + pessoa.upper() + ". Gostaria de aprender Python hoje?") # APRESENTAÇÃO DE VARIÁVEL EM MAIÚSCULA
print("Olá, " + pessoa.lower() + ". Gostaria de aprender Python hoje?") # APRESENTAÇÃO DE VARIÁVEL EM MINÚSCULA

###

print('Albert Einstein certa vez disse: "Uma pessoa que nunca cometeu um erro \njamais tentou algo novo."') # APRESENTAÇÃO DE UMA CITAÇÃO FAMOSA

###

famous_person = "albert einstein"
message = "Uma pessoa que nunca cometeu um erro \njamais tentou algo novo"  # REPETINDO O EXERCÍCIO ANTERIOR USANDO OUTROS MÉTODOS

print(famous_person.title() + ' certa vez disse: "' + message + '."')

###

famous_person = " albert einstein  "

print("Meu nome é " + famous_person.lstrip() + ".")
print("Meu nome é " + famous_person.rstrip() + ".") # REMOVENDO ESPAÇOS EM BRANCO
print("Meu nome é " + famous_person.strip() + ".")

famous_person = "\tEinstein,\n\tDarwin,\n\tNewton." # USANDO TUBULAÇÕES E QUEBRAS DE PÁGINA
print(famous_person)