"""Implemente uma função que recebe um número N e retorna uma lista com os N primeiros termos da sequência de Fibonacci."""

def fibonacci(n):
    seq = [0, 1]  # começamos com os dois primeiros termos
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])  # soma os dois últimos
    return seq[:n]  # garante que só devolve N termos

# Exemplo:
print(fibonacci(10))  # → [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

"""
Resumo:
- Sequência começa em [0, 1].
- Cada termo é a soma dos dois anteriores.
- Usamos .append() para adicionar novos termos.
"""
