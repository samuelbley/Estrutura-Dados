# Crie uma classe chamada Produto com os atributos: nome, preco e quantidade.
# Use o método __init__ para inicializar esses atributos.
# Depois, crie dois produtos diferentes e imprima seus dados.

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

produto1 = Produto("Notebook", 3500.00, 5)
produto2 = Produto("Mouse Gamer", 150.00, 12)

print(produto1.nome, produto1.preco, produto1.quantidade)
print(produto2.nome, produto2.preco, produto2.quantidade)