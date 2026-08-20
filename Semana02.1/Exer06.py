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


def maiores(lst, n):

    atual = lst
    quantidade = 0

    while atual is not None:

        if atual.info > n:
            quantidade += 1

        atual = atual.proximo

    return quantidade


def ultimo(lista):

    if lista is None:
        return None

    atual = lista

    while atual.proximo is not None:
        atual = atual.proximo

    return atual


def lista_insere_final(lst, valor):

    novo = Lista(valor)

    if lst is None:
        return novo

    atual = lst

    while atual.proximo is not None:
        atual = atual.proximo

    atual.proximo = novo

    return lst


def lista_calcula_media(lst):

    if lst is None:
        return 0

    atual = lst
    soma = 0
    quantidade = 0

    while atual is not None:

        soma += atual.info
        quantidade += 1

        atual = atual.proximo

    return soma / quantidade


def lista_altera(lst):

    atual = lst

    while atual is not None:

        atual.info = -atual.info

        atual = atual.proximo

    return lst


lista = None

while True:

    print("\n===== MENU =====")
    print("1 - Inserir item no início")
    print("2 - Listar itens")
    print("3 - Remover item")
    print("4 - Contar maiores que n")
    print("5 - Mostrar último elemento")
    print("6 - Inserir item no final")
    print("7 - Calcular média")
    print("8 - Alterar sinais")
    print("0 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:

        valor = float(input("Digite o valor: "))
        lista = lista_insere(lista, valor)

    elif opcao == 2:

        lista_imprime(lista)

    elif opcao == 3:

        valor = float(input("Digite o valor para remover: "))
        lista = lista_retira(lista, valor)

    elif opcao == 4:

        n = float(input("Digite o valor de n: "))

        resultado = maiores(lista, n)

        print("Quantidade de valores maiores que", n, ":", resultado)

    elif opcao == 5:

        ultimo_no = ultimo(lista)

        if ultimo_no is None:
            print("Lista vazia.")
        else:
            print("Último elemento:", ultimo_no.info)

    elif opcao == 6:

        valor = float(input("Digite o valor: "))
        lista = lista_insere_final(lista, valor)

    elif opcao == 7:

        if lista is None:
            print("Lista vazia.")
        else:
            media = lista_calcula_media(lista)
            print("Média:", media)

    elif opcao == 8:

        lista = lista_altera(lista)

        print("Sinais alterados!")

    elif opcao == 0:

        print("Programa encerrado.")
        break

    else:

        print("Opção inválida!")