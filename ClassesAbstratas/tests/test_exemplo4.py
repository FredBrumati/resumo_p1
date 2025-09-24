import pytest
from exemplo4 import Produto, Carrinho

def test_adicionar_e_total():
    p1 = Produto("Camisa", 50)
    p2 = Produto("Calça", 100)
    c = Carrinho()
    c.adicionar(p1)
    c.adicionar(p2)
    assert c.total() == 150

def test_remover_produto():
    p = Produto("Tênis", 200)
    c = Carrinho()
    c.adicionar(p)
    c.remover(p)
    assert c.total() == 0

def test_desconto():
    p = Produto("Camisa", 100)
    p.desconto(10)
    assert p.preco == 90

def test_alterar_preco():
    p = Produto("Boné", 50)
    p.alterar_preco(70)
    assert p.preco == 70

def test_finalizar_compra():
    p = Produto("Bermuda", 80)
    c = Carrinho()
    c.adicionar(p)
    msg = c.finalizar_compra()
    assert msg == "Compra finalizada. Total pago: R$80.00"
    assert c.total() == 0
