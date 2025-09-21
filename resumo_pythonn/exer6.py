"""Escreva uma função que verifica se uma string fornecida pelo usuário é
um palíndromo (lê-se igual de frente para trás e de trás para frente)."""

# Função que verifica se uma string é um palíndromo
def eh_palindromo(texto):
    # .lower() → deixa tudo minúsculo
    # .replace(" ", "") → remove espaços para não atrapalhar
    texto_limpo = texto.lower().replace(" ", "")
    
    # Verificamos se o texto é igual ao seu reverso [::-1]
    return texto_limpo == texto_limpo[::-1]

# Entrada do usuário
palavra = input("Digite uma palavra ou frase: ")

if eh_palindromo(palavra):
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")

"""
Resumo da lógica:
- Palíndromo = palavra ou frase que se lê igual de frente para trás.
- Exemplo: "arara", "radar", "A sacada da casa".
- [::-1] → fatia a string de trás pra frente (inversão).
- Normalizamos o texto (minúsculo e sem espaços) para evitar erros.
"""
