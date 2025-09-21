"""Peça ao usuário para inserir um texto e conte quantas vezes cada palavra
aparece nele. Exiba os resultados em um dicionário."""

# Programa para contar quantas vezes cada palavra aparece em um texto

# Entrada do usuário
texto = input("Digite um texto: ")

# Quebramos o texto em palavras separadas pelo espaço usando .split()
palavras = texto.split()

# Criamos um dicionário para armazenar as palavras e suas contagens
contagem = {}

# Percorremos cada palavra da lista
for palavra in palavras:
    if palavra in contagem:
        contagem[palavra] += 1  # se já existe no dicionário, soma +1
    else:
        contagem[palavra] = 1   # se não existe ainda, adiciona com valor 1

# Exibindo o resultado
print("Contagem de palavras:", contagem)

"""
Resumo da lógica:
- .split() divide o texto em palavras (por padrão, separa por espaço).
- Usamos um dicionário para guardar pares {palavra: quantidade}.
- Verificamos se a palavra já existe no dicionário:
   → se sim, aumentamos o valor (+1).
   → se não, criamos a chave com valor 1.
"""
