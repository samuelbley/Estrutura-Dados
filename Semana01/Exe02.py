# Adicione à classe Produto um método chamado calcular_total() 
# que retorna o valor total em estoque (preco * quantidade).
# Depois, mostre o total de um produto.

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_total(self):
        return self.preco * self.quantidade

produto1 = Produto("Notebook", 3500.00, 5)
produto2 = Produto("Mouse Gamer", 150.00, 12)

total_p1 = produto1.calcular_total()
print("Total do produto 1:", total_p1)

print("Total do produto 2:", produto2.calcular_total())
