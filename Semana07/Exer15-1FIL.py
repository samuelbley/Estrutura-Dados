class Fila:
    def __init__(self):
        self.elementos = []

    def enfileirar(self, usuario):
        self.elementos.append(usuario)

    def desenfileirar(self):
        if len(self.elementos) == 0:
            return None

        return self.elementos.pop(0)

    def percorrer(self):
        for usuario in self.elementos:
            print(usuario)


fila = Fila()

while True:
    print("1 - Adicionar usuário")
    print("2 - Atender usuário")
    print("3 - Mostrar fila")
    print("4 - Sair")

    opcao = int(input("Escolha: "))

    if opcao == 1:
        usuario = input("Digite o usuário: ")
        fila.enfileirar(usuario)

    elif opcao == 2:
        usuario = fila.desenfileirar()

        if usuario is None:
            print("Fila vazia")
        else:
            print("Usuário atendido:", usuario)

    elif opcao == 3:
        fila.percorrer()

    elif opcao == 4:
        break