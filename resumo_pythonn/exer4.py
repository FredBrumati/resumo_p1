"""Implemente uma função recursiva para calcular o fatorial de um número
fornecido pelo usuário."""

# Função recursiva para calcular o fatorial
def fatorial(n):
    # Caso base: fatorial de 0 ou 1 é 1
    if n == 0 or n == 1:
        return 1
    else:
        # Passo recursivo: n * fatorial(n-1)
        return n * fatorial(n - 1)

# Entrada do usuário
num = int(input("Digite um número para calcular o fatorial: "))

print(f"O fatorial de {num} é {fatorial(num)}")

"""
Resumo da lógica:
- Recursão = função que chama a si mesma.
- Caso base: quando n == 0 ou n == 1, retorna 1 (para parar a recursão).
- Caso geral: fatorial(n) = n * fatorial(n-1).
Exemplo: fatorial(5) = 5 * 4 * 3 * 2 * 1.
"""
