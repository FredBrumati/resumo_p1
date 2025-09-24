"""Loja com Estoque
Classe base Produto:
info()
desconto(porcentagem)
alterar_preco(valor)
Classe Carrinho:
adicionar(produto)
remover(produto)
total()
finalizar_compra()
Já virou quase um mini-sistema, com métodos que mudam estado."""

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def info(self):
        return f"{self.nome} - R${self.preco:.2f}"

    def desconto(self, porcentagem):
        self.preco *= (1 - porcentagem / 100)

    def alterar_preco(self, novo_preco):
        self.preco = novo_preco

class Carrinho:
    def __init__(self):
        self.itens = []

    def adicionar(self, produto):
        self.itens.append(produto)

    def remover(self, produto):
        self.itens.remove(produto)

    def total(self):
        return sum(item.preco for item in self.itens)

    def finalizar_compra(self):
        valor = self.total()
        self.itens.clear()
        return f"Compra finalizada. Total pago: R${valor:.2f}"

# Teste
p1 = Produto("Camisa", 50)
p2 = Produto("Calça", 100)
carrinho = Carrinho()

carrinho.adicionar(p1)
carrinho.adicionar(p2)
print("Total:", carrinho.total())
p1.desconto(10)
print("Total com desconto:", carrinho.total())
print(carrinho.finalizar_compra())
