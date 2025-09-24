"""Exercício 3 – Decorator de Tentativas
Enunciado:
Crie um decorator chamado tentativas que tenta executar uma função até 3 vezes caso ocorra um erro (Exception).
Use-o em duas funções:
divisao(a, b) → faz a divisão de a por b.
abrir_arquivo(nome) → tenta abrir um arquivo texto."""

def tentativas(func):
    def wrapper(*args, **kwargs):
        for i in range(3):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"Tentativa {i+1} falhou: {e}")
        raise Exception("Número máximo de tentativas atingido!")
    return wrapper

@tentativas
def divisao(a, b):
    return a / b

@tentativas
def abrir_arquivo(nome):
    with open(nome, "r") as f:
        return f.read()

print(divisao(10, 2))
# print(divisao(10, 0))  # gera tentativas e falha
