"""Exercício 3 – Escola
Implemente um sistema escolar em Python utilizando classes abstratas:
Crie uma classe abstrata Pessoa com atributos nome e idade.
Essa classe deve possuir os seguintes métodos:
Um método abstrato atividade(), que será definido pelas subclasses.
Um método concreto info(), que retorna nome e idade.
Crie as subclasses:
Aluno, que possui uma lista de notas. Deve implementar os métodos:
atividade() → retorna "Aluno estudando".
adicionar_nota(valor) → adiciona nota à lista.
media() → calcula a média das notas.
status() → retorna "Aprovado" se a média ≥ 6, senão "Reprovado".
Professor, que deve implementar:
atividade() → retorna "Professor ensinando".
atribuir_nota(aluno, valor) → adiciona uma nota ao aluno.
No programa principal, crie professores e alunos, adicione notas e verifique o status dos alunos."""

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
