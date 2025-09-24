"""Escola com Notas
Classe base Pessoa:
info()
atividade() (abstrato)
Subclasse Aluno:
adicionar_nota(valor)
media()
status() → aprovado ou reprovado
Subclasse Professor:
atribuir_nota(aluno, valor)
Aqui temos métodos interagindo entre objetos."""

from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def atividade(self):
        pass

class Aluno(Pessoa):
    def __init__(self, nome):
        super().__init__(nome)
        self.notas = []

    def atividade(self):
        return f"{self.nome} está estudando."

    def adicionar_nota(self, valor):
        self.notas.append(valor)

    def media(self):
        return sum(self.notas) / len(self.notas) if self.notas else 0

    def status(self):
        return "Aprovado" if self.media() >= 6 else "Reprovado"

class Professor(Pessoa):
    def atividade(self):
        return f"{self.nome} está dando aula."

    def atribuir_nota(self, aluno, valor):
        aluno.adicionar_nota(valor)
        return f"{self.nome} atribuiu nota {valor} para {aluno.nome}."

# Teste
aluno = Aluno("Pedro")
prof = Professor("Carla")

print(prof.atividade())
print(aluno.atividade())
print(prof.atribuir_nota(aluno, 8))
print(prof.atribuir_nota(aluno, 5))
print("Média:", aluno.media())
print("Status:", aluno.status())
