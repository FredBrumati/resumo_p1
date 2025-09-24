"""Biblioteca
Classe base Publicacao:
info() → mostra título e autor
emprestar() → muda atributo disponivel = False
devolver() → muda disponivel = True
Subclasses (Livro, Revista) só mudam a forma como descrevem o tipo.
Aqui já temos 3 métodos concretos além de tipo()."""

from abc import ABC, abstractmethod

class Publicacao(ABC):
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    @abstractmethod
    def tipo(self):
        pass

    def info(self):
        return f"{self.tipo()} - {self.titulo}, de {self.autor}. Disponível: {self.disponivel}"

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            return f"{self.titulo} foi emprestado."
        return f"{self.titulo} já está emprestado!"

    def devolver(self):
        self.disponivel = True
        return f"{self.titulo} foi devolvido."

class Livro(Publicacao):
    def tipo(self):
        return "Livro"

class Revista(Publicacao):
    def tipo(self):
        return "Revista"

# Teste
livro = Livro("Python Básico", "Maria")
revista = Revista("Ciência Hoje", "João")

print(livro.info())
print(livro.emprestar())
print(livro.info())
print(livro.devolver())
print(revista.info())
