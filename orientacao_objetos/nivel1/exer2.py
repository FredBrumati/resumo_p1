"""2.Carrinho de Compras
Implemente as classes Item(nome, preco, qtd) e Carrinho. O carrinho deve permitir adicionar itens e calcular o valor total."""

# Classe que representa um item no carrinho
class Item:
    def __init__(self, nome, preco, qtd):
        self.nome = nome
        self.preco = preco
        self.qtd = qtd

    def subtotal(self):
        # Retorna o preço total desse item (preço * quantidade)
        return self.preco * self.qtd


# Classe que representa o carrinho de compras
class Carrinho:
    def __init__(self):
        # O carrinho guarda uma lista de itens
        self.itens = []

    def adicionar_item(self, item):
        # item é um objeto da classe Item
        self.itens.append(item)

    def calcular_total(self):
        # Soma o subtotal de todos os itens do carrinho
        return sum(item.subtotal() for item in self.itens)

    def listar_itens(self):
        # Mostra todos os itens do carrinho
        for item in self.itens:
            print(f"{item.nome} - {item.qtd} x R${item.preco:.2f} = R${item.subtotal():.2f}")


# ---------------- PROGRAMA PRINCIPAL ----------------
if __name__ == "__main__":
    # Criando itens
    item1 = Item("Arroz", 20.0, 2)
    item2 = Item("Feijão", 8.5, 3)
    item3 = Item("Leite", 4.75, 5)

    # Criando carrinho e adicionando itens
    carrinho = Carrinho()
    carrinho.adicionar_item(item1)
    carrinho.adicionar_item(item2)
    carrinho.adicionar_item(item3)

    # Listando itens e mostrando total
    carrinho.listar_itens()
    print(f"\nTotal da compra: R${carrinho.calcular_total():.2f}")
