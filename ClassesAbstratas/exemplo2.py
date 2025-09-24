"""Exercício 2 – Conta Bancária
Implemente um sistema de contas bancárias em Python utilizando classes abstratas:
Crie uma classe abstrata Conta com atributos numero (inteiro) e saldo (float).
Essa classe deve possuir os seguintes métodos:
Um método abstrato operacao(valor) que será definido pelas subclasses.
Um método info(), que retorna as informações da conta.
Um método depositar(valor), que adiciona saldo.
Um método sacar(valor), que diminui saldo caso haja dinheiro suficiente.
Um método transferir(valor, outra_conta), que transfere valores entre contas.
Crie a subclasse ContaCorrente, que implementa operacao(valor) realizando um saque.
Crie a subclasse ContaPoupanca, que implementa operacao(valor) aplicando um rendimento de 5% sobre o saldo.
No programa principal, crie contas e teste as operações."""

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
