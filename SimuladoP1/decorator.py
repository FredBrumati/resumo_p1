"""Exercício 3

Crie um decorator em Python chamado valida_positivo que verifica se todos os argumentos numéricos de uma função são positivos:

Se todos os argumentos forem válidos, a função deve ser executada normalmente.
Se algum argumento for negativo, deve ser levantado um ValueError.
Use esse decorator em pelo menos duas funções:
raiz_quadrada(x), que retorna a raiz quadrada de x.
divisao(a, b), que retorna o resultado de a / b.
Teste chamando as funções com valores positivos (funciona normalmente) e valores negativos (gera erro)."""

def valida_positivo(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if arg < 0:
                raise ValueError('Número negativo!')
        response = func(*args, **kwargs)
        for key in kwargs:
            if kwargs[key]< 0:
                raise ValueError('num vai da')
        return response
    return wrapper

@valida_positivo
def raiz_quadrada(a):
    print(a ** 0.5)

raiz_quadrada(3)
raiz_quadrada(a=5)