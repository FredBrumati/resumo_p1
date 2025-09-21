"""1.Conta Bancária
Implemente a classe Conta com atributos numero, titular e saldo (inicial em 0). Métodos: depositar, sacar, extrato. 
O saque não pode deixar o saldo negativo."""

# Classe básica em Python
class Pessoa:
    def __init__(self, nome, idade):
        # Atributos (características do objeto)
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        # Método (comportamento do objeto)
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."

# Programa principal
p1 = Pessoa("Ana", 20)
print(p1.apresentar())

# --- RESUMO ---
# class NomeClasse:  → cria uma classe
# __init__           → método construtor, executado ao criar o objeto
# self.atributo      → representa características do objeto
# métodos (def)      → funções ligadas à classe
