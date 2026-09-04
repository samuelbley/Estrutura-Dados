class Atleta:
    def __init__(self, id):
        self.id = id
        self.bastao = False
        self.anterior = None
        self.proximo = None


class ListaCircular:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0

    def adicionar(self, id):
        novo = Atleta(id)

        if self.inicio is None:
            self.inicio = novo
            novo.proximo = novo
            novo.anterior = novo
        else:
            ultimo = self.inicio.anterior

            novo.proximo = self.inicio
            novo.anterior = ultimo

            ultimo.proximo = novo
            self.inicio.anterior = novo

        self.tamanho += 1
        print("Atleta adicionado.")

    def remover(self, id):
        if self.inicio is None:
            print("Lista vazia.")
            return

        atual = self.inicio

        while True:
            if atual.id == id:
                break

            atual = atual.proximo

            if atual == self.inicio:
                print("Atleta não encontrado.")
                return

        if self.tamanho == 1:
            self.inicio = None
        else:
            atual.anterior.proximo = atual.proximo
            atual.proximo.anterior = atual.anterior

            if atual == self.inicio:
                self.inicio = atual.proximo

        self.tamanho -= 1
        print("Atleta removido.")

    def mostrar(self):
        if self.inicio is None:
            print("Lista vazia.")
            return

        atual = self.inicio

        while True:
            print("ID:", atual.id, "| Bastão:", atual.bastao)

            atual = atual.proximo

            if atual == self.inicio:
                break

    def simular(self, voltas):
        if self.inicio is None:
            print("Não há atletas.")
            return

        atual = self.inicio

        inicio = self.inicio

        while True:
            atual.bastao = False
            atual = atual.proximo

            if atual == inicio:
                break

        atual = self.inicio
        atual.bastao = True

        total_turnos = self.tamanho * voltas

        for turno in range(total_turnos):
            print("Turno", turno + 1, "- Atleta", atual.id, "está com o bastão.")

            atual.bastao = False
            atual = atual.proximo
            atual.bastao = True


lista = ListaCircular()

while True:
    print("\n===== MENU =====")
    print("1 - Adicionar atleta")
    print("2 - Remover atleta")
    print("3 - Mostrar atletas")
    print("4 - Simular bastão")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        id = int(input("Digite o ID do atleta: "))
        lista.adicionar(id)

    elif opcao == "2":
        id = int(input("Digite o ID do atleta: "))
        lista.remover(id)

    elif opcao == "3":
        lista.mostrar()

    elif opcao == "4":
        voltas = int(input("Digite quantas voltas deseja simular: "))
        lista.simular(voltas)

    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")