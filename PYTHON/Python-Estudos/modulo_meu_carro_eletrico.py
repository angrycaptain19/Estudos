from modulo_carro_eletrico import Carro_Elétrico

meu_tesla = Carro_Elétrico(
        fabricante='tesla', modelo='model s', ano=2016
        )

print(meu_tesla.nome_descritivo())
meu_tesla.bateria.descrição_bateria()
meu_tesla.bateria.obter_alcance()