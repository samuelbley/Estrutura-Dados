class Fila:
    def __init__(self):
        self.elementos = []

    def enfileirar(self, tempo):
        self.elementos.append(tempo)

    def desenfileirar(self):
        if self.esta_vazia():
            return None

        return self.elementos.pop(0)

    def percorrer(self):
        for tempo in self.elementos:
            print(tempo)

    def frente(self):
        if self.esta_vazia():
            return None

        return self.elementos[0]

    def esta_vazia(self):
        return len(self.elementos) == 0

    def tamanho(self):
        return len(self.elementos)


def media(fila):
    if fila.esta_vazia():
        return 0

    total = sum(fila.elementos)

    return total / fila.tamanho()


fila = Fila()

fila.enfileirar(10)
fila.enfileirar(20)
fila.enfileirar(15)
fila.enfileirar(25)

print("Tamanho:", fila.tamanho())
print("Tempo médio de espera:", media(fila))