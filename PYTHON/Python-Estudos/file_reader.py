# USANDO UM Path Relativo
with open('ARQUIVOS_TEXTO/pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)

# USANDO UM Path Absoluto
arquivo_path = 'C:/Users/alber/OneDrive/Documentos/PYTHON/ARQUIVOS_TEXTO/pi_digits.txt'
with open(arquivo_path) as file_object:
    contents = file_object.read()
    print(contents)

# LENDO DADOS LINHA A LINHA
filename = 'ARQUIVOS_TEXTO/pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# CRIANDO UMA LISTA DE LINHAS DE UM ARQUIVO
filename = 'ARQUIVOS_TEXTO/pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

# TRABALHANDO COM O CONTEÚDO DE UM ARQUIVO
filename = 'ARQUIVOS_TEXTO/pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''.join(line.strip() for line in lines)
print(pi_string)
print(len(pi_string))

# ARQUIVOS GRANDES: UM MILHÃO DE DÍGITOS
filename = 'ARQUIVOS_TEXTO/CURSO_EXTENSIVO_PYTHON/chapter_10/pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''.join(line.strip() for line in lines)
print(pi_string[:52] + "...")
print(len(pi_string))

# SEU ANIVERSÁRIO ESTÁ CONTIDO EM pi?
filename = 'ARQUIVOS_TEXTO/CURSO_EXTENSIVO_PYTHON/chapter_10/pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Nos forneça sua data de nascimento, na forma ddmmaa: ")
if birthday in pi_string:
    print("Sua data de nascimento aparece no primeiro milhão de"
        " dígitos de pi.")
else:
    print("Sua data de nascimento não aparece no primeiro milhão de"
        " dígitos de pi.")