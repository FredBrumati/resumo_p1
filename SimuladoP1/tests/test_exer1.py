"""Exercício 2 
Utilizando o sistema de transporte do Exercício 1, crie testes unitários em Python com pytest: 
Teste se um objeto Carro(5) possui capacidade igual a 5. 
Teste se o método mover() de Carro retorna a string correta. 
Teste se o método mover() de Bicicleta retorna a string correta. 
Crie também um teste de falha proposital para verificar se a criação de um Carro com capacidade 
negativa (Carro(-3)) gera um erro ou comportamento esperado."""

from exer1 import *
import pytest

carro = Carro(5)
bicicleta = Bicicleta(1)

def test_capacidade_carro():
    assert carro.capacidade == 5

def test_mover_carro():
    assert carro.mover() == "O carro está se movendo com: 5 pessoas"

def test_mover_bicicleta():
    assert bicicleta.mover() == "A bicicleta está se movendo com: 1 pessoas"

def test_carro_capacidade_negativa():
    with pytest.raises(ValueError):
        Carro(-3)