import pytest
from exemplo3 import *

def test_divisao_sucesso():
    assert divisao(10, 2) == 5

def test_divisao_zero():
    with pytest.raises(Exception):
        divisao(10, 0)
