"""Crie um programa que lê um arquivo .txt e conta quantas linhas, palavras e
caracteres ele contém."""

# Programa que lê um arquivo .txt e conta linhas, palavras e caracteres

def analisar_arquivo(nome_arquivo):
    with open(nome_arquivo, "r", encoding="utf-8") as f:
        texto = f.read()  # lê todo o conteúdo do arquivo
    
    # Contagem
    num_linhas = texto.count("\n") + 1 if texto else 0  # cada quebra de linha conta +1
    num_palavras = len(texto.split())   # split separa o texto em palavras
    num_caracteres = len(texto)         # len() dá o total de caracteres
    
    return num_linhas, num_palavras, num_caracteres

# Teste (substitua 'arquivo.txt' pelo nome real do seu arquivo)
linhas, palavras, caracteres = analisar_arquivo("arquivo.txt")

print(f"Linhas: {linhas}")
print(f"Palavras: {palavras}")
print(f"Caracteres: {caracteres}")

"""
Resumo da lógica:
- open("arquivo.txt", "r") → abre o arquivo em modo leitura.
- .read() → lê todo o conteúdo do arquivo.
- .split() → divide o texto em palavras (separadas por espaços).
- .count("\n") → conta quantas quebras de linha existem.
- len(texto) → dá o número de caracteres.
"""
