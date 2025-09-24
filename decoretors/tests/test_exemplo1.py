from exemplo1 import *
import pytest

def test_soma():
    assert soma(3, 4) == 7

def test_potencia():
    assert potencia(2, 5) == 32
