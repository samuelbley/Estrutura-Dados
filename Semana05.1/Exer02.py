class No:
    def __init__(self, parada):
        self.parada = parada
        self.proximo = None
        self.anterior = None


def inserir(cabeca, parada):
    novo = No(parada)

    if cabeca is None:
        novo.proximo = novo
        novo.anterior = novo
        cabeca = novo
        return cabeca

    novo.proximo = cabeca
    novo.anterior = cabeca.anterior
    cabeca.anterior.proximo = novo
    cabeca.anterior = novo
    cabeca = novo

    return cabeca


def listar(cabeca):
    if cabeca is None:
        print("Lista vazia")
        return

    aux = cabeca

    while True:
        print("-", aux.parada)

        if aux.proximo == cabeca:
            return

        aux = aux.proximo


def remover(cabeca, parada):
    if cabeca is None:
        print("Lista vazia")
        return cabeca

    aux = cabeca

    while True:
        if aux.parada == parada:

            if aux.proximo == aux:
                return None

            aux.anterior.proximo = aux.proximo
            aux.proximo.anterior = aux.anterior

            if aux == cabeca:
                cabeca = aux.proximo

            return cabeca

        if aux.proximo == cabeca:
            print("Parada não encontrada")
            return cabeca

        aux = aux.proximo


def simular(cabeca):
    if cabeca is None:
        print("Lista vazia")
        return

    aux = cabeca

    while True:
        print("Ônibus na parada:", aux.parada)

        aux = aux.proximo

        if aux == cabeca:
            return


def menu():
    print("\n1 - Adicionar parada")
    print("2 - Listar paradas")
    print("3 - Remover parada")
    print("4 - Simular percurso")
    print("5 - Sair")

    opcao = int(input("Digite uma opção: "))

    return opcao


def main():
    cabeca = None
    opcao = 0

    while opcao != 5:
        opcao = menu()

        if opcao == 1:
            parada = int(input("Digite o número da parada: "))
            cabeca = inserir(cabeca, parada)

        elif opcao == 2:
            listar(cabeca)

        elif opcao == 3:
            parada = int(input("Digite a parada que deseja remover: "))
            cabeca = remover(cabeca, parada)

        elif opcao == 4:
            simular(cabeca)

        elif opcao == 5:
            print("Programa encerrado")

        else:
            print("Opção inválida")


main()