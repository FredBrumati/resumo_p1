"""Escreva uma função que receba dois números inteiros e retorne uma lista
contendo todos os números primos entre eles."""

# Função para verificar se um número é primo
def eh_primo(n):
    # Números menores que 2 não são primos
    if n < 2:
        return False
    # Verificamos divisores de 2 até n-1
    for i in range(2, n):
        if n % i == 0:  # se for divisível, não é primo
            return False
    return True  # se não achou divisor, é primo

# Função para retornar a lista de primos entre dois números
def primos_entre(a, b):
    lista_primos = []
    for num in range(a, b + 1):  # percorre do menor até o maior número
        if eh_primo(num):
            lista_primos.append(num)  # adiciona na lista se for primo
    return lista_primos

# Teste
x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))

print("Primos entre", x, "e", y, ":", primos_entre(x, y))

"""
Resumo da lógica:
- Criamos uma função eh_primo() que retorna True se o número for primo.
- Um número é primo se só tem dois divisores: 1 e ele mesmo.
- A função primos_entre(a, b) percorre os números do intervalo e usa eh_primo().
- Os números primos encontrados são adicionados em uma lista.
- Por fim, retornamos essa lista.
"""
