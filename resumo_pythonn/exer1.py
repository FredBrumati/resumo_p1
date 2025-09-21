"""Escreva um programa que verifica se um número fornecido pelo usuário
é perfeito. Um número é perfeito quando a soma de seus divisores (exceto
ele mesmo) é igual ao próprio número."""

# Programa para verificar se um número é perfeito

# Um número perfeito é aquele em que a soma dos divisores (excluindo ele mesmo)
# é igual ao próprio número.
# Exemplo: 6 → divisores: 1, 2, 3 → 1+2+3 = 6 → número perfeito

# Entrada do usuário
num = int(input("Digite um número: "))

# Variável para guardar a soma dos divisores
soma_divisores = 0

# Percorre de 1 até num-1 (porque não inclui o próprio número)
for i in range(1, num):
    if num % i == 0:   # verifica se i é divisor
        soma_divisores += i  # soma os divisores encontrados

# Verificação se é perfeito
if soma_divisores == num:
    print(num, "é um número perfeito.")
else:
    print(num, "não é um número perfeito.")

"""
Resumo da lógica:
- Usamos um laço for para percorrer de 1 até num-1.
- O operador % (módulo) verifica se o número é divisível por i.
- Se for, somamos esse divisor.
- No final, comparamos a soma com o número original.
"""
