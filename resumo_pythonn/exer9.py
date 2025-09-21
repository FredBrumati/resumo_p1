"""Implemente um sistema simples de CRUD usando um dicionário, onde o usuário pode adicionar, remover, atualizar e listar contatos (nome e telefone)."""

def menu():
    contatos = {}

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
            contatos[nome] = tel  # adiciona ou atualiza
        elif opcao == "2":
            nome = input("Nome para remover: ")
            contatos.pop(nome, None)  # remove se existir
        elif opcao == "3":
            nome = input("Nome: ")
            if nome in contatos:
                tel = input("Novo telefone: ")
                contatos[nome] = tel
        elif opcao == "4":
            for nome, tel in contatos.items():
                print(nome, ":", tel)
        elif opcao == "5":
            break

"""
Resumo:
- Usamos um dicionário {nome: telefone}.
- .pop(chave) → remove contato.
- .items() → percorre nome e telefone.
"""
