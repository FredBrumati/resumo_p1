from exemplo5 import *
import pytest

def test_fib():
    assert fib(10) == 55  # 10º termo da sequência de Fibonacci

def test_quadrado():
    assert quadrado(6) == 36
