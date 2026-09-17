# PILHA Implemente um programa que simule o funcionamento de operações 
# matemáticas armazenadas em uma pilha. O menu deve conter as opções:

# Inserir operação na pilha (ex: “5+3”, “7*2”)
# Retirar última operação (POP)
# Mostrar última operação inserida (topo)
# Mostrar todas as operações pendentes
# Sair

class Operacao:
    def __init__(self, operacao):
        self.operacao = operacao
        self.proximo = None


def menu():
    print("====MENU====")
    print("1 - Inserir operação")
    print("2 - Retirar última operação")
    print("3 - Mostrar última operação inserida")
    print("4 - Mostrar operações")
    print("5 - Sair")
    opc = int(input("Digite a opção desejada: "))
    return opc


def inserir_operacao(ultimo, operacao):
    novo = Operacao(operacao)
    if ultimo == None:
        return novo

    novo.proximo = ultimo
    ultimo = novo
    return novo


def retirar_ultima_operacao(ultimo):
    if ultimo == None:
        print("Pilha de operações vazia")
        return None

    removido = ultimo
    ultimo = ultimo.proximo
    print("Operação retirada:", removido.operacao)
    return ultimo


def mostrar_ultima_operacao(ultimo):
    if ultimo == None:
        print("Pilha de operações vazia")
    else:
        print("Última operação inserida:", ultimo.operacao)


def mostrar_todas_operacoes(ultimo):
    if ultimo == None:
        print("Pilha de operações vazia")
        return

    aux = ultimo
    contador = 1
    while aux != None:
        print(contador, "-", aux.operacao)
        contador += 1
        aux = aux.proximo


def main():
    ultimo = None
    opcao = 0
    while opcao != 5:
        opcao = menu()
        if opcao == 1:
            operacao = input("Digite a operação (ex: 5+3): ")
            ultimo = inserir_operacao(ultimo, operacao)
        elif opcao == 2:
            ultimo = retirar_ultima_operacao(ultimo)
        elif opcao == 3:
            mostrar_ultima_operacao(ultimo)
        elif opcao == 4:
            mostrar_todas_operacoes(ultimo)
        elif opcao == 5:
            print("Encerrando...")
        else:
            print("Opção inválida")


main()