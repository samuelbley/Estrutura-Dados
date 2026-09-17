# PILHA Os carros entram em uma garagem em fila indiana (um atrás do outro). 
# Para um carro sair, é necessário retirar todos os que entraram depois 
# dele (LIFO). Para isso, faça um algoritmo que já tenha cadastrado 20 
# carros. Depois peça para o usuário qual ele deseja tirar. Assim, você 
# deverá tirar todos os outros que entraram na fila depois dele. Mostre 
# todos os carros retirados.

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self.proximo = None


def inserir_carro(ultimo, nome):
    novo = Carro(nome)
    novo.proximo = ultimo
    return novo


def retirar_carro(ultimo):
    if ultimo is None:
        print("Garagem vazia.")
        return None

    aux = ultimo
    i = 1
    while aux is not None:
        print(i, "-", aux.nome)
        aux = aux.proximo
        i += 1

    posicao = int(input("Digite o número do carro que deseja retirar: "))

    removidos = []
    aux = ultimo
    contador = 1
    while aux is not None and contador < posicao:
        removidos.append(aux.nome)
        aux = aux.proximo
        contador += 1

    if aux is None:
        print("Posição inválida.")
        return 

    print("Carros retirados:", removidos)
    print("Carro liberado:", aux.nome)
    return aux


def main():
    ultimo = None
    ultimo = inserir_carro(ultimo, "Fusca")
    ultimo = inserir_carro(ultimo, "Gol")
    ultimo = inserir_carro(ultimo, "Civic")
    ultimo = inserir_carro(ultimo, "Corolla")
    ultimo = inserir_carro(ultimo, "Onix")
    ultimo = inserir_carro(ultimo, "HB20")
    ultimo = inserir_carro(ultimo, "Palio")
    ultimo = inserir_carro(ultimo, "Uno")
    ultimo = inserir_carro(ultimo, "Celta")
    ultimo = inserir_carro(ultimo, "Ka")
    ultimo = inserir_carro(ultimo, "Fiesta")
    ultimo = inserir_carro(ultimo, "Sandero")
    ultimo = inserir_carro(ultimo, "Logan")
    ultimo = inserir_carro(ultimo, "Cruze")
    ultimo = inserir_carro(ultimo, "Jetta")
    ultimo = inserir_carro(ultimo, "Polo")
    ultimo = inserir_carro(ultimo, "Voyage")
    ultimo = inserir_carro(ultimo, "Prisma")
    ultimo = inserir_carro(ultimo, "Argo")
    ultimo = inserir_carro(ultimo, "Mobi")

    ultimo = retirar_carro(ultimo)


main()