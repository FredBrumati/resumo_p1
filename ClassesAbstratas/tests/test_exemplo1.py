import pytest
from exemplo1 import Livro, Revista

def test_criar_livro():
    livro = Livro("Python Básico", "Maria")
    assert livro.titulo == "Python Básico"
    assert livro.autor == "Maria"
    assert livro.disponivel is True

def test_emprestar_livro():
    livro = Livro("Python Básico", "Maria")
    assert livro.emprestar() == "Python Básico foi emprestado."
    assert livro.disponivel is False

def test_devolver_livro():
    livro = Livro("Python Básico", "Maria")
    livro.emprestar()  # primeiro empresta
    assert livro.devolver() == "Python Básico foi devolvido."
    assert livro.disponivel is True

def test_info_revista():
    revista = Revista("Ciência Hoje", "João")
    assert revista.info() == "Revista - Ciência Hoje, de João. Disponível: True"

# Teste de falha proposital: criar um livro sem título (por exemplo) gera erro
def test_criar_livro_sem_titulo():
    with pytest.raises(TypeError):
        Livro()
