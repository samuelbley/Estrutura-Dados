class Pilha:
    def __init__(self):
        self.elementos = []

    def empilhar(self, dado):
        self.elementos.append(dado)

    def desempilhar(self):
        if self.esta_vazia():
            return None

        return self.elementos.pop()

    def percorrer(self):
        for elemento in self.elementos:
            print(elemento)

    def topo(self):
        if self.esta_vazia():
            return None

        return self.elementos[-1]

    def esta_vazia(self):
        return len(self.elementos) == 0

    def tamanho(self):
        return len(self.elementos)


def media(pilha):
    if pilha.esta_vazia():
        return 0

    total = sum(pilha.elementos)

    return total / pilha.tamanho()


pilha = Pilha()

pilha.empilhar(10)
pilha.empilhar(20)
pilha.empilhar(30)
pilha.empilhar(40)

print("Tamanho:", pilha.tamanho())
print("Média:", media(pilha))