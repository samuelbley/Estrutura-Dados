
class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def exibir_informacoes(self):
        print("Nome:", self.nome)
        print("Preço:", self.preco)
        print("Quantidade em estoque:", self.quantidade)
        print("Valor total em estoque:", self.calcular_valor_total())

    def adicionar_estoque(self, quantidade):
        self.quantidade += quantidade

    def vender(self, quantidade):
        if quantidade <= self.quantidade:
            self.quantidade -= quantidade
            print("Venda realizada com sucesso.")
        else:
            print("Estoque insuficiente.")

    def calcular_valor_total(self):
        return self.preco * self.quantidade


produto1 = Produto("Arroz", 25.00, 10)
produto2 = Produto("Feijão", 8.00, 15)
produto3 = Produto("Macarrão", 5.00, 20)

while True:
    print("\n===== MENU =====")
    print("1 - Produto 1")
    print("2 - Produto 2")
    print("3 - Produto 3")
    print("4 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 4:
        print("Programa encerrado.")
        break

    if opcao == 1:
        produto = produto1
    elif opcao == 2:
        produto = produto2
    elif opcao == 3:
        produto = produto3
    else:
        print("Opção inválida.")
        continue

    while True:
        print("\n===== MENU DO PRODUTO =====")
        print("1 - Exibir informações")
        print("2 - Adicionar estoque")
        print("3 - Realizar venda")
        print("4 - Calcular valor total")
        print("5 - Voltar")

        opcao_produto = int(input("Escolha uma opção: "))

        if opcao_produto == 1:
            produto.exibir_informacoes()

        elif opcao_produto == 2:
            quantidade = int(input("Quantidade para adicionar: "))
            produto.adicionar_estoque(quantidade)
            print("Estoque atualizado.")

        elif opcao_produto == 3:
            quantidade = int(input("Quantidade para vender: "))
            produto.vender(quantidade)

        elif opcao_produto == 4:
            print("Valor total em estoque:", produto.calcular_valor_total())

        elif opcao_produto == 5:
            break

        else:
            print("Opção inválida.")
