"""Exercício 1 – Biblioteca
Implemente um sistema de publicações em Python utilizando classes abstratas:
Crie uma classe abstrata Publicacao com atributos titulo, autor e disponivel (inicialmente True).
Essa classe deve possuir os seguintes métodos:
Um método abstrato tipo(), que será implementado nas subclasses.
Um método concreto info(), que retorna as informações da publicação.
Um método emprestar(), que marca a publicação como não disponível.
Um método devolver(), que marca a publicação como disponível novamente.
Crie duas subclasses:
Livro, que retorna "Livro: <titulo> de <autor>".
Revista, que retorna "Revista: <titulo> de <autor>".
No programa principal, crie objetos de Livro e Revista, adicione-os a uma lista e teste os métodos criados."""

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

def main():
    livro = Livro("Python Básico", "Maria")
    revista = Revista("Ciência Hoje", "João")

    publicacoes = [livro, revista]

    for pub in publicacoes:
        print(pub.info())
        print(pub.emprestar())
        print(pub.info())
        print(pub.devolver())
        print(pub.info())
        print("-" * 40)

if __name__ == "__main__":
    main()
