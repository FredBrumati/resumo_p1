"""Exercício 3

Crie um decorator em Python chamado valida_positivo que verifica se todos os argumentos numéricos de uma função são positivos:

Se todos os argumentos forem válidos, a função deve ser executada normalmente.
Se algum argumento for negativo, deve ser levantado um ValueError.
Use esse decorator em pelo menos duas funções:
raiz_quadrada(x), que retorna a raiz quadrada de x.
divisao(a, b), que retorna o resultado de a / b.
Teste chamando as funções com valores positivos (funciona normalmente) e valores negativos (gera erro)."""

# Decorator que valida se os argumentos são positivos
def valida_positivo(func):
    def wrapper(*args, **kwargs):
        # Verificação em argumentos posicionais (*args)
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError("Número negativo não permitido!")

        # Verificação em argumentos nomeados (**kwargs)
        for key, value in kwargs.items():
            if isinstance(value, (int, float)) and value < 0:
                raise ValueError("Número negativo não permitido!")

        return func(*args, **kwargs)
    return wrapper

@valida_positivo
def raiz_quadrada(x):
    return x ** 0.5

@valida_positivo
def divisao(a, b):
    return a / b

# ---- Testes ----
print("Raiz quadrada de 9:", raiz_quadrada(9))    # válido
print("Divisão 10/2:", divisao(10, 2))            # válido

# Testes que vão gerar erro
# raiz_quadrada(-4)         # gera ValueError
# divisao(-10, 2)           # gera ValueError
# divisao(a=10, b=-5)       # gera ValueError
