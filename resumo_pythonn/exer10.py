"""Utilizando o exercício 9, altere o armazenamento para um arquivo local."""

import json

def salvar(contatos):
    with open("contatos.json", "w") as f:
        json.dump(contatos, f)

def carregar():
    try:
        with open("contatos.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def menu():
    contatos = carregar()
    
    while True:
        print("\n1. Adicionar contato")
        print("2. Remover contato")
        print("3. Atualizar contato")
        print("4. Listar contatos")
        print("5. Sair")
        
        opcao = input("Escolha: ")

        if opcao == "1":
            nome = input("Nome: ")
            tel = input("Telefone: ")
            contatos[nome] = tel
        elif opcao == "2":
            nome = input("Nome para remover: ")
            contatos.pop(nome, None)
        elif opcao == "3":
            nome = input("Nome: ")
            if nome in contatos:
                tel = input("Novo telefone: ")
                contatos[nome] = tel
        elif opcao == "4":
            for nome, tel in contatos.items():
                print(nome, ":", tel)
        elif opcao == "5":
            salvar(contatos)
            break

"""
Resumo:
- json.dump() → salva dicionário em arquivo.
- json.load() → carrega de volta.
- Usamos try/except para evitar erro se o arquivo não existir.
"""
