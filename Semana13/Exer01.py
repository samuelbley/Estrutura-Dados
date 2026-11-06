# Uma agência de viagens temporais utiliza uma fila especial para controlar 
# os viajantes que entrarão na máquina do tempo. Como algumas missões são 
# urgentes, viajantes podem entrar tanto no início quanto no final da fila.
# Crie um algoritmo utilizando a estrutura deque da biblioteca collections 
# e apresente o seguinte menu:
# 1 - Adicionar viajante no início da fila
# 2 - Adicionar viajante no final da fila
# 3 - Enviar viajante do início para a missão
# 4 - Enviar viajante do final para a missão
# 5 - Apresentar fila de viajantes
# 6 - Sair
# Regras:
# Os nomes dos viajantes devem ser armazenados em um deque.
# Ao remover um viajante, exiba o nome da pessoa enviada para a missão.
# Caso a fila esteja vazia, apresente uma mensagem adequada.
# Utilize funções para cada operação.
# O main deve conter apenas o menu, o laço de repetição, as estruturas de 
# condição e as chamadas das funções.

from collections import deque

class Viajante:
    def __init__(self, nome):
        self.nome = nome

class Fila:
    def __init__(self):
        self.fila = deque()

    def adc_inicio(self):
        nome = input("Digite o nome do viajante: ")
        novo_viajante = Viajante(nome)
        self.fila.appendleft(novo_viajante)

    def adc_final(self):
        nome = input("Digite o nome do viajante: ")
        novo_viajante = Viajante(nome)
        self.fila.append(novo_viajante)

    def remover_inicio(self):
        if len(self.fila) > 0:
            nome_viajante = self.fila.popleft()
            print(f"Viajante {nome_viajante.nome} enviado pra missão!")
        else:
            print("A fila está vazia")

    def remover_final(self):
        if len(self.fila) > 0:
            nome_viajante = self.fila.pop()
            print(f"Viajante {nome_viajante.nome} enviado pra missão!")
        else: 
            print("A fila está vazia")

    def apresentar_fila(self):
        if len(self.fila) > 0:
            aux = 0

            while aux < len(self.fila):
                print(self.fila[aux].nome)
                aux += 1
        else: 
            print("A fila está vazia!")

def main():
    opc = 0
    fila = Fila()

    while opc != 6:
        print("====> MENU <====")
        print("1 - Adicionar viajante no início da fila")
        print("2 - Adicionar viajante no final da fila")
        print("3 - Enviar viajante do início para a missão")
        print("4 - Enviar viajante do final para a missão")
        print("5 - Apresentar fila de viajantes")
        print("6 - Sair")
        opc = int(input("Digite a opção desejada: "))
        if opc == 1:
            fila.adc_inicio()
        elif opc == 2:
            fila.adc_final()
        elif opc == 3:
            fila.remover_inicio()
        elif opc == 4:
            fila.remover_final()
        elif opc == 5:
            fila.apresentar_fila()
        elif opc == 6:
            print("Encerrando o programa...")
        else:
            print("Opção inválida!")

main()
