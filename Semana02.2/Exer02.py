
class ContaBancaria:
    def __init__(self, titular, numero, saldo):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo

    def consultar_saldo(self):
        print("Titular:", self.titular)
        print("Número da conta:", self.numero)
        print("Saldo: R$", self.saldo)

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print("Depósito realizado com sucesso.")
        else:
            print("O valor deve ser maior que zero.")

    def sacar(self, valor):
        if valor <= 0:
            print("O valor deve ser maior que zero.")
        elif valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor
            print("Saque realizado com sucesso.")

    def transferir(self, valor, conta_destino):
        if valor <= 0:
            print("O valor deve ser maior que zero.")
        elif valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor
            conta_destino.saldo += valor
            print("Transferência realizada com sucesso.")


conta1 = ContaBancaria("João", 1001, 1000.00)
conta2 = ContaBancaria("Maria", 1002, 500.00)

while True:
    print("\n===== MENU =====")
    print("1 - Consultar conta 1")
    print("2 - Consultar conta 2")
    print("3 - Depositar")
    print("4 - Sacar")
    print("5 - Transferir")
    print("6 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        conta1.consultar_saldo()

    elif opcao == 2:
        conta2.consultar_saldo()

    elif opcao == 3:
        conta = int(input("Escolha a conta (1 ou 2): "))
        valor = float(input("Digite o valor do depósito: "))

        if conta == 1:
            conta1.depositar(valor)
        elif conta == 2:
            conta2.depositar(valor)
        else:
            print("Conta inválida.")

    elif opcao == 4:
        conta = int(input("Escolha a conta (1 ou 2): "))
        valor = float(input("Digite o valor do saque: "))

        if conta == 1:
            conta1.sacar(valor)
        elif conta == 2:
            conta2.sacar(valor)
        else:
            print("Conta inválida.")

    elif opcao == 5:
        origem = int(input("Conta de origem (1 ou 2): "))
        destino = int(input("Conta de destino (1 ou 2): "))
        valor = float(input("Digite o valor da transferência: "))

        if origem == 1 and destino == 2:
            conta1.transferir(valor, conta2)
        elif origem == 2 and destino == 1:
            conta2.transferir(valor, conta1)
        else:
            print("Contas inválidas.")

    elif opcao == 6:
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")
