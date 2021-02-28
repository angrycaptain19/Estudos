class Funcionario():
    """Coleta dados dos funcionários."""

    def __init__(self, nome, sobrenome, salario):
        """Gerando atributos para cada parâmetro relacionado."""
        self.nome = nome
        self.sobrenome = sobrenome
        self.salario = salario


    def receber_aumento(self, aumento=5000):
        """Soma 5 mil dólares ao salário anual."""
        self.salario += aumento