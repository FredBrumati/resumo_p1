import pytest
from exemplo2 import ContaCorrente

def test_depositar():
    conta = ContaCorrente(101, 100)
    assert conta.depositar(50) == "Depositado R$50.00"
    assert conta.saldo == 150

def test_sacar_sucesso():
    conta = ContaCorrente(101, 100)
    assert conta.sacar(50) == "Saque de R$50.00 realizado."
    assert conta.saldo == 50

def test_sacar_insuficiente():
    conta = ContaCorrente(101, 30)
    assert conta.sacar(100) == "Saldo insuficiente!"

def test_transferir():
    c1 = ContaCorrente(101, 200)
    c2 = ContaCorrente(102, 100)
    msg = c1.transferir(50, c2)
    assert msg == "Transferido R$50.00 para conta 102."
    assert c1.saldo == 150
    assert c2.saldo == 150
