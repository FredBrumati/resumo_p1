import pytest
from exemplo1 import Livro, Revista

def test_criar_livro():
    livro = Livro("Python", "Maria")
    assert livro.titulo == "Python"
    assert livro.disponivel is True

def test_emprestar_e_devolver():
    livro = Livro("Python", "Maria")
    assert livro.emprestar() == "Python foi emprestado."
    assert livro.disponivel is False
    assert livro.devolver() == "Python foi devolvido."
    assert livro.disponivel is True

def test_revista_info():
    revista = Revista("Ciência Hoje", "João")
    assert "Revista" in revista.info()
