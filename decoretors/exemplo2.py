"""Exercício 2 – Decorator de Tempo de Execução

Enunciado:
Crie um decorator chamado tempo_execucao que mede e imprime quanto tempo uma função leva para ser executada.
Use-o em duas funções:

contar_ate(n) → imprime de 1 até n.

fatorial(n) → calcula o fatorial recursivamente."""

import time

def tempo_execucao(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        print(f"{func.__name__} executou em {fim - inicio:.5f} segundos")
        return resultado
    return wrapper

@tempo_execucao
def contar_ate(n):
    for i in range(1, n+1):
        pass
    return n

@tempo_execucao
def fatorial(n):
    return 1 if n == 0 else n * fatorial(n-1)

print(contar_ate(1000000))
print(fatorial(10))
