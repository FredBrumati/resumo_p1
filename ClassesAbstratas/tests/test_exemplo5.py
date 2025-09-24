import pytest
from exemplo5 import Carro, Bicicleta

def test_carro_mover_com_sucesso():
    carro = Carro(5, 10)
    msg = carro.mover(50)  # consumo 5 litros
    assert msg == "Carro andou 50km. Combustível restante: 5.0L"
    assert carro.combustivel == 5

def test_carro_combustivel_insuficiente():
    carro = Carro(5, 2)
    msg = carro.mover(50)  # precisa de 5 litros
    assert msg == "Combustível insuficiente!"
    assert carro.combustivel == 2

def test_abastecer():
    carro = Carro(5, 5)
    msg = carro.abastecer(10)
    assert msg == "Abastecido 10L. Total: 15.0L"
    assert carro.combustivel == 15

def test_status_combustivel():
    carro = Carro(5, 8)
    assert carro.status_combustivel() == "Combustível disponível: 8.0L"

def test_bicicleta_mover():
    bike = Bicicleta(1)
    msg = bike.mover(20)
    assert msg == "Bicicleta andou 20km. Nível de desgaste: 1.0"
    assert bike.desgaste == 1.0

def test_status_desgaste():
    bike = Bicicleta(1)
    bike.mover(10)
    assert bike.status_desgaste() == "Desgaste atual: 0.5"
