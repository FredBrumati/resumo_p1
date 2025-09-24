"""Conta Bancária Avançada
Classe base Conta:
info()
depositar(valor)
sacar(valor)
transferir(valor, outra_conta)
Ou seja, a herança continua, mas a classe tem operações extras."""

from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, numero, saldo=0):
        self.numero = numero
        self.saldo = saldo

    def info(self):
        return f"Conta {self.numero} | Saldo: R${self.saldo:.2f}"

    def depositar(self, valor):
        self.saldo += valor
        return f"Depositado R${valor:.2f}"

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return f"Saque de R${valor:.2f} realizado."
        return "Saldo insuficiente!"

    def transferir(self, valor, outra_conta):
        if valor <= self.saldo:
            self.sacar(valor)
            outra_conta.depositar(valor)
            return f"Transferido R${valor:.2f} para conta {outra_conta.numero}."
        return "Transferência não realizada, saldo insuficiente!"

class ContaCorrente(Conta):
    pass

# Teste
c1 = ContaCorrente(101, 500)
c2 = ContaCorrente(102, 200)

print(c1.info())
print(c1.transferir(150, c2))
print(c1.info())
print(c2.info())
