import modulo_carro
import modulo_carro_eletrico

meu_beetle = modulo_carro.Carro(
        fabricante='volkswagen', modelo='beetle', ano=2016        
        )
print(meu_beetle.nome_descritivo())

meu_tesla = modulo_carro_eletrico.Carro_Elétrico(
        fabricante='tesla', modelo='roadster', ano=2016
        )
print(meu_tesla.nome_descritivo())