import pytest
from exemplo5 import Carro, Bicicleta

def test_carro_mover_com_sucesso():
    carro = Carro(5, 10)
    msg = carro.mover(50)  # consumo 5 litros
    assert "Carro andou 50km" in msg
    assert carro.combustivel == 5

def test_carro_combustivel_insuficiente():
    carro = Carro(5, 2)
    msg = carro.mover(50)  # precisa de 5 litros
    assert msg == "Combustível insuficiente!"
    assert carro.combustivel == 2

def test_abastecer():
    carro = Carro(5, 5)
    msg = carro.abastecer(10)
    assert "Abastecido 10L" in msg
    assert carro.combustivel == 15

def test_bicicleta_mover():
    bike = Bicicleta(1)
    msg = bike.mover(20)
    assert "Bicicleta andou 20km" in msg
    assert bike.desgaste > 0
