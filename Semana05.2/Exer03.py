import random


class Guerreiro:
    def __init__(self, guerreiro):
        self.guerreiro = guerreiro
        self.proximo = None
        self.anterior = None

    def inserir_guerreiros(self, quantidade):
        for i in range(2, quantidade + 1):
            novo = Guerreiro("G" + str(i))

            ultimo = self.anterior

            ultimo.proximo = novo
            novo.anterior = ultimo
            novo.proximo = self
            self.anterior = novo

    def contar(self):
        quantidade = 1
        atual = self.proximo

        while atual != self:
            quantidade += 1
            atual = atual.proximo

        return quantidade

    def remover(self, guerreiro):
        guerreiro.anterior.proximo = guerreiro.proximo
        guerreiro.proximo.anterior = guerreiro.anterior

    def roleta(self):
        quantidade = self.contar()
        atual = self

        while quantidade > 1:
            posicao = random.randint(1, quantidade)

            for i in range(posicao - 1):
                atual = atual.proximo

            print("Eliminado:", atual.guerreiro)

            proximo = atual.proximo

            self.remover(atual)

            atual = proximo
            quantidade -= 1

        print("Sobrevivente:", atual.guerreiro)


def main():
    quantidade = int(input("Quantidade de guerreiros: "))

    if quantidade < 2:
        print("Quantidade inválida.")
    else:
        cabeca = Guerreiro("G1")
        cabeca.proximo = cabeca
        cabeca.anterior = cabeca

        cabeca.inserir_guerreiros(quantidade)
        cabeca.roleta()


main()