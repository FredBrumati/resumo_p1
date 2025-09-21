from decorators import *
import pytest

def test_raiz_quadrada():
    assert raiz_quadrada(9) == 3

def test_divisao():
    assert divisao(10, 2) == 5

def test_raiz_quadrada_negativo():
    with pytest.raises(ValueError):
        raiz_quadrada(-9)

def test_divisao_negativa():
    with pytest.raises(ValueError):
        divisao(-10, 2)