class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.proximo = None
        self.anterior = None

    def adicionar(self, nome):
        novo = Cliente(nome)

        ultimo = self.anterior

        ultimo.proximo = novo
        novo.anterior = ultimo
        novo.proximo = self
        self.anterior = novo

    def remover(self, nome):
        atual = self

        while True:
            if atual.nome == nome:
                atual.anterior.proximo = atual.proximo
                atual.proximo.anterior = atual.anterior
                return

            atual = atual.proximo

            if atual == self:
                break

    def passar_pizza(self, vezes):
        atual = self

        for i in range(vezes):
            print("Recebendo pizza:", atual.nome)
            atual = atual.proximo


def main():
    cabeca = Cliente("Samuel")
    cabeca.proximo = cabeca
    cabeca.anterior = cabeca

    cabeca.adicionar("Pedro")
    cabeca.adicionar("João")
    cabeca.adicionar("Maria")

    print("Passagem da pizza:")
    cabeca.passar_pizza(10)

    print()

    cabeca.remover("João")

    print("Após João sair:")
    cabeca.passar_pizza(10)


main()