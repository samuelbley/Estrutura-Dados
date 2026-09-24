class Fila:
    def __init__(self):
        self.elementos = []

    def enfileirar(self, usuario):
        self.elementos.append(usuario)

    def desenfileirar(self):
        if self.esta_vazia():
            return None

        return self.elementos.pop(0)

    def percorrer(self):
        for usuario in self.elementos:
            print(usuario)

    def frente(self):
        if self.esta_vazia():
            return None

        return self.elementos[0]

    def esta_vazia(self):
        return len(self.elementos) == 0


fila = Fila()

fila.enfileirar("João")
fila.enfileirar("Pedro")
fila.enfileirar("Carlos")

print("Próximo usuário:", fila.frente())

fila.desenfileirar()

print("Próximo usuário:", fila.frente())

print("Fila vazia:", fila.esta_vazia())