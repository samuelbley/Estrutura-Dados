class Lista:
    def __init__(self, info=None):
        self.info = info
        self.proximo = None


def lista_insere(lista, valor):
    novo = Lista(valor)
    novo.proximo = lista
    return novo


def lista_imprime(lista):
    atual = lista

    while atual is not None:
        print(atual.info)
        atual = atual.proximo


def lista_retira(lista, valor):
    atual = lista
    anterior = None

    while atual is not None:

        if atual.info == valor:

            if anterior is None:
                return atual.proximo

            anterior.proximo = atual.proximo
            return lista

        anterior = atual
        atual = atual.proximo

    return lista


lista = None

while True:

    print("\n1. Inserir item")
    print("2. Listar itens")
    print("3. Remover item")
    print("0. Sair")

    opcao = int(input("Escolha: "))

    if opcao == 1:
        valor = float(input("Digite o valor: "))
        lista = lista_insere(lista, valor)

    elif opcao == 2:
        lista_imprime(lista)

    elif opcao == 3:
        valor = float(input("Digite o valor para remover: "))
        lista = lista_retira(lista, valor)

    elif opcao == 0:
        break

    else:
        print("Opção inválida!")