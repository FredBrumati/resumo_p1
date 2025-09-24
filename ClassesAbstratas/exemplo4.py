"""Exercício 4 – Loja com Carrinho
Implemente um sistema de compras em Python utilizando orientação a objetos:
Crie a classe Produto com atributos nome e preco.
Essa classe deve possuir os métodos:
info(), que retorna o nome e preço do produto.
desconto(porcentagem), que aplica desconto sobre o preço.
alterar_preco(valor), que define um novo preço.
Crie a classe Carrinho, que mantém uma lista de produtos. Ela deve ter os métodos:
adicionar(produto) → adiciona produto ao carrinho.
remover(produto) → remove produto do carrinho.
total() → retorna o valor total da compra.
finalizar_compra() → retorna o valor total pago e esvazia o carrinho.
No programa principal, crie produtos, adicione-os ao carrinho, calcule o total e finalize a compra."""

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
