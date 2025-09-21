"""Crie um programa que recebe uma lista de nomes e sorteia um nome"""

import random

def sorteia_nome(lista_nomes):
    return random.choice(lista_nomes)  # escolhe 1 nome aleatório

# Exemplo:
nomes = ["Ana", "Carlos", "Maria", "João"]
print("Nome sorteado:", sorteia_nome(nomes))

"""
Resumo:
- random.choice(lista) → retorna um elemento aleatório da lista.
"""
