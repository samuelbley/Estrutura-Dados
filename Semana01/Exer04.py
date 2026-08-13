# Crie uma classe chamada Produto, que tenha os atributos: nome, 
# preço e quantidade em estoque.
# Implemente um método atualizar_estoque() que recebe um valor e 
# soma à quantidade atual.
# Crie dois objetos e atualize o estoque de cada um, mostrando os 
# dados antes e depois da atualização.

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_total(self):
        return self.preco * self.quantidade

    def atualizar_estoque(self, valor):
        self.quantidade += valor

produto1 = Produto("Notebook", 3500.00, 5)
produto2 = Produto("Mouse Gamer", 150.00, 12)

print("--- ANTES ---")
print(produto1.nome, "- Estoque:", produto1.quantidade)
print(produto2.nome, "- Estoque:", produto2.quantidade)

produto1.atualizar_estoque(3)
produto2.atualizar_estoque(10)

print("\n--- DEPOIS ---")
print(produto1.nome, "- Estoque:", produto1.quantidade)
print(produto2.nome, "- Estoque:", produto2.quantidade)