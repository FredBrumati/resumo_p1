from exemplo2 import *
import pytest

def test_contar_ate():
    assert contar_ate(1000) == 1000

def test_fatorial():
    assert fatorial(5) == 120
