# Um banco tem dois tipos de clientes: preferenciais e comuns.

# Clientes comuns entram no final da fila.
# Clientes preferenciais entram no início.
# Quando um atendimento ocorre, o cliente do início da fila é atendido (removido).
# O programa deve mostrar sempre a ordem atual de atendimento.

from collections import deque

class Banco:
    def __init__(self):
        self.fila = deque()

    def adicionar_comum(self):
        nome = input("Digite o nome do cliente comum: ")
        self.fila.append(nome)
        print("Cliente comum adicionado ao fim da fila.")

    def adicionar_preferencial(self):
        nome = input("Digite o nome do cliente preferencial: ")
        self.fila.appendleft(nome)
        print("Cliente preferencial adicionado ao início da fila.")

    def atender(self):
        if self.fila:
            cliente = self.fila.popleft()
            print(f"Cliente {cliente} atendido.")
        else:
            print("A fila está vazia.")

    def listar(self):
        if self.fila:
            print("\nOrdem atual de atendimento:")
            for cliente in self.fila:
                print(cliente)
        else:
            print("A fila está vazia.")


def main():
    banco = Banco()
    opcao = 0

    while opcao != 4:
        print("\n---- MENU DO BANCO ----")
        print("1 - Adicionar cliente comum")
        print("2 - Adicionar cliente preferencial")
        print("3 - Atender próximo cliente")
        print("4 - Sair do sistema")

        try:
            opcao = int(input("Digite a opção desejada: "))
        except ValueError:
            print("Digite uma opção válida.")
            continue

        if opcao == 1:
            banco.adicionar_comum()
            banco.listar()

        elif opcao == 2:
            banco.adicionar_preferencial()
            banco.listar()

        elif opcao == 3:
            banco.atender()
            banco.listar()

        elif opcao == 4:
            print("Saindo do sistema.")

        else:
            print("Opção inválida.")


main()