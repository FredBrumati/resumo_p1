"""Exercício 5 – Decorator de Cache
Enunciado:
Crie um decorator chamado cache_resultado que armazena resultados de chamadas anteriores de uma função para evitar recomputação.
Use-o em duas funções:
fib(n) → retorna o n-ésimo número de Fibonacci.
quadrado(x) → retorna o quadrado de um número."""

def cache_resultado(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            print(f"Usando cache para {func.__name__}{args}")
            return cache[args]
        resultado = func(*args)
        cache[args] = resultado
        return resultado
    return wrapper

@cache_resultado
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

@cache_resultado
def quadrado(x):
    return x * x

print(fib(10))
print(fib(10))  # usa cache
print(quadrado(5))
print(quadrado(5))  # usa cache
