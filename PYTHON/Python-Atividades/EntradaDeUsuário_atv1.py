# LOCAÇÃO DE AUTOMÓVEIS
carro = input("Em qual carro você está interessado? ")
print("\nDeixe-me ver se consigo um " + carro.title() + " pra você.")

# LUGARES EM UM RESTAURANTE
acentos = input("\nOlá. Quantos acentos você deseja pra sua mesa? ")
acentos = int(acentos)

if acentos < 2:
    print("\nSua mesa está pronta. Sirva-se e acomode-se!")
elif acentos < 8:
    print("\nSua mesa está pronta. Sirvam-se e acomodem-se!")
else:
    print("\nSinto muito. Vocês devem esperar um pouco.")

# MULTIPLOS DE DEZ
numero = input("\nPor favor, informe um número para verificarmos se ele é multiplo de 10: ")
numero = int(numero)

if numero % 10 == 0:
    print("\nO número " + str(numero) + " é divisivel por 10.")
else:
    print("\nO número " + str(numero) + " não é divisivel por 10.")