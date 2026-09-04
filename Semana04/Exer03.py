<<<<<<< HEAD
class No:
    def __init__(self, valor):
        self.valor = valor
        self.anterior = None
        self.proximo = None


class ListaDuplamenteEncadeada:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.quantidade = 0

    def inserir_inicio(self, valor):
        novo = No(valor)

        if self.inicio is None:
            self.inicio = novo
            self.fim = novo
        else:
            novo.proximo = self.inicio
            self.inicio.anterior = novo
            self.inicio = novo

        self.quantidade += 1

    def inserir_final(self, valor):
        novo = No(valor)

        if self.fim is None:
            self.inicio = novo
            self.fim = novo
        else:
            novo.anterior = self.fim
            self.fim.proximo = novo
            self.fim = novo

        self.quantidade += 1

    def exibir_inicio_fim(self):
        if self.inicio is None:
            print("Lista vazia.")
            return

        atual = self.inicio

        while atual:
            print(atual.valor)
            atual = atual.proximo

    def exibir_fim_inicio(self):
        if self.fim is None:
            print("Lista vazia.")
            return

        atual = self.fim

        while atual:
            print(atual.valor)
            atual = atual.anterior

    def remover(self, valor):
        atual = self.inicio

        while atual:
            if atual.valor == valor:
                if atual.anterior:
                    atual.anterior.proximo = atual.proximo
                else:
                    self.inicio = atual.proximo

                if atual.proximo:
                    atual.proximo.anterior = atual.anterior
                else:
                    self.fim = atual.anterior

                self.quantidade -= 1
                print("Elemento removido com sucesso.")
                return

            atual = atual.proximo

        print("Elemento não encontrado.")


lista = ListaDuplamenteEncadeada()

for i in range(6):
    valor = input(f"Digite o {i + 1}º valor: ")
    lista.inserir_final(valor)

while True:
    print("\n1 - Inserir no início")
    print("2 - Inserir no final")
    print("3 - Exibir do primeiro até o último")
    print("4 - Exibir do último até o primeiro")
    print("5 - Remover elemento")
    print("0 - Sair")

    opcao = int(input("Escolha: "))

    if opcao == 1:
        valor = input("Valor: ")
        lista.inserir_inicio(valor)
    elif opcao == 2:
        valor = input("Valor: ")
        lista.inserir_final(valor)
    elif opcao == 3:
        lista.exibir_inicio_fim()
    elif opcao == 4:
        lista.exibir_fim_inicio()
    elif opcao == 5:
        valor = input("Valor a remover: ")
        lista.remover(valor)
    elif opcao == 0:
        break
    else:
=======
class No:
    def __init__(self, valor):
        self.valor = valor
        self.anterior = None
        self.proximo = None


class ListaDuplamenteEncadeada:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.quantidade = 0

    def inserir_inicio(self, valor):
        novo = No(valor)

        if self.inicio is None:
            self.inicio = novo
            self.fim = novo
        else:
            novo.proximo = self.inicio
            self.inicio.anterior = novo
            self.inicio = novo

        self.quantidade += 1

    def inserir_final(self, valor):
        novo = No(valor)

        if self.fim is None:
            self.inicio = novo
            self.fim = novo
        else:
            novo.anterior = self.fim
            self.fim.proximo = novo
            self.fim = novo

        self.quantidade += 1

    def exibir_inicio_fim(self):
        if self.inicio is None:
            print("Lista vazia.")
            return

        atual = self.inicio

        while atual:
            print(atual.valor)
            atual = atual.proximo

    def exibir_fim_inicio(self):
        if self.fim is None:
            print("Lista vazia.")
            return

        atual = self.fim

        while atual:
            print(atual.valor)
            atual = atual.anterior

    def remover(self, valor):
        atual = self.inicio

        while atual:
            if atual.valor == valor:
                if atual.anterior:
                    atual.anterior.proximo = atual.proximo
                else:
                    self.inicio = atual.proximo

                if atual.proximo:
                    atual.proximo.anterior = atual.anterior
                else:
                    self.fim = atual.anterior

                self.quantidade -= 1
                print("Elemento removido com sucesso.")
                return

            atual = atual.proximo

        print("Elemento não encontrado.")


lista = ListaDuplamenteEncadeada()

for i in range(6):
    valor = input(f"Digite o {i + 1}º valor: ")
    lista.inserir_final(valor)

while True:
    print("\n1 - Inserir no início")
    print("2 - Inserir no final")
    print("3 - Exibir do primeiro até o último")
    print("4 - Exibir do último até o primeiro")
    print("5 - Remover elemento")
    print("0 - Sair")

    opcao = int(input("Escolha: "))

    if opcao == 1:
        valor = input("Valor: ")
        lista.inserir_inicio(valor)
    elif opcao == 2:
        valor = input("Valor: ")
        lista.inserir_final(valor)
    elif opcao == 3:
        lista.exibir_inicio_fim()
    elif opcao == 4:
        lista.exibir_fim_inicio()
    elif opcao == 5:
        valor = input("Valor a remover: ")
        lista.remover(valor)
    elif opcao == 0:
        break
    else:
>>>>>>> b8ffbb4f4b6e3adb9bb985b77ac8557328ba63c9
        print("Opção inválida.")