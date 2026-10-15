# Implemente um programa em Python que simule um sistema de gerenciamento s
# de chamados de TI utilizando um deque.
# O sistema deve apresentar um menu interativo com as seguintes opções:

# Adicionar chamado no fim da fila (chamado comum).
# Adicionar chamado no início da fila (chamado urgente).
# Atender chamado do início da fila (remoção do primeiro).
# Atender chamado do fim da fila (remoção do último).
# Listar todos os chamados da fila.
# Sair do sistema.


class Chamado:
    def __init__(self, nome):
        self.nome = nome
        self.proximo = None
        self.anterior = None


class Deque:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def inserir_fim(self, nome):
        novo = Chamado(nome)

        if self.inicio is None:
            self.inicio = self.fim = novo
        else:
            novo.anterior = self.fim
            self.fim.proximo = novo
            self.fim = novo

        print(f"Chamado {nome} inserido no fim da fila.")

    def inserir_inicio(self, nome):
        novo = Chamado(nome)

        if self.inicio is None:
            self.inicio = self.fim = novo
        else:
            novo.proximo = self.inicio
            self.inicio.anterior = novo
            self.inicio = novo

        print(f"Chamado {nome} inserido no início da fila.")

    def atender_inicio(self):
        if self.inicio is None:
            print("A fila está vazia.")
        else:
            nome = self.inicio.nome
            self.inicio = self.inicio.proximo

            if self.inicio is None:
                self.fim = None
            else:
                self.inicio.anterior = None

            print(f"Chamado {nome} atendido.")

    def atender_fim(self):
        if self.fim is None:
            print("A fila está vazia.")
        else:
            nome = self.fim.nome
            self.fim = self.fim.anterior

            if self.fim is None:
                self.inicio = None
            else:
                self.fim.proximo = None

            print(f"Chamado {nome} atendido.")

    def listar(self):
        if self.inicio is None:
            print("A fila está vazia.")
            return

        print("Listagem do primeiro chamado até o último:")

        aux = self.inicio
        contador = 1

        while aux is not None:
            print(f"{contador} - {aux.nome}")
            contador += 1
            aux = aux.proximo


def main():
    opcao = 0
    fila = Deque()

    while opcao != 6:
        print("\n---- MENU ----")
        print("1 - Adicionar chamado no fim da fila (chamado comum)")
        print("2 - Adicionar chamado no início da fila (chamado urgente)")
        print("3 - Atender chamado do início da fila (remoção do primeiro)")
        print("4 - Atender chamado do fim da fila (remoção do último)")
        print("5 - Listar todos os chamados da fila")
        print("6 - Sair do sistema")

        try:
            opcao = int(input("Digite a opção desejada: "))
        except ValueError:
            print("Digite uma opção válida.")
            continue

        if opcao == 1:
            nome = input("Digite o nome do chamado: ")
            fila.inserir_fim(nome)

        elif opcao == 2:
            nome = input("Digite o nome do chamado urgente: ")
            fila.inserir_inicio(nome)

        elif opcao == 3:
            fila.atender_inicio()

        elif opcao == 4:
            fila.atender_fim()

        elif opcao == 5:
            fila.listar()

        elif opcao == 6:
            print("Saindo do sistema...")

        else:
            print("Opção inválida.")


main()
