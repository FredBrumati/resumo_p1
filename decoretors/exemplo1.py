"""Exercício 1 – Decorator de Log de Execução
Enunciado:
Crie um decorator chamado log_execucao que imprime o nome da função e os argumentos com os quais ela foi chamada, antes de executá-la.
Use-o em duas funções:
soma(a, b) → retorna a soma.
potencia(base, exp) → retorna a base elevada ao expoente."""

def log_execucao(func):
    def wrapper(*args, **kwargs):
        print(f"Executando {func.__name__} com args={args}, kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_execucao
def soma(a, b):
    return a + b

@log_execucao
def potencia(base, exp):
    return base ** exp

print(soma(3, 4))
print(potencia(2, 5))
