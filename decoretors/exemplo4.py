"""Exercício 4 – Decorator de Autorização
Enunciado:
Crie um decorator chamado precisa_autorizacao que verifica se o usuário tem permissão para acessar uma função.
Use-o em duas funções:
ver_dados(usuario) → retorna "Dados confidenciais".
editar_dados(usuario) → retorna "Dados editados com sucesso"."""

def precisa_autorizacao(func):
    def wrapper(usuario, *args, **kwargs):
        if not usuario.get("autorizado", False):
            raise PermissionError("Acesso negado!")
        return func(usuario, *args, **kwargs)
    return wrapper

@precisa_autorizacao
def ver_dados(usuario):
    return "Dados confidenciais"

@precisa_autorizacao
def editar_dados(usuario):
    return "Dados editados com sucesso"

usuario1 = {"nome": "Ana", "autorizado": True}
usuario2 = {"nome": "João", "autorizado": False}

print(ver_dados(usuario1))
# print(ver_dados(usuario2))  # gera erro de permissão
