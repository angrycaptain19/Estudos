from modulo_carro import Carro

meu_novo_carro = Carro(
        fabricante='audi', modelo='a4', ano=2016
        )
print(meu_novo_carro.nome_descritivo())

meu_novo_carro.leitura_hodometro = 23
meu_novo_carro.ler_hodometro()