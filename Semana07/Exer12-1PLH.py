class Pilha:
    def __init__(self):
        self.elementos = []

    def empilhar(self, dado):
        self.elementos.append(dado)

    def desempilhar(self):
        if len(self.elementos) == 0:
            return None

        return self.elementos.pop()

    def percorrer(self):
        for elemento in self.elementos:
            print(elemento)


pilha = Pilha()

pilha.empilhar(10)
pilha.empilhar(20)
pilha.empilhar(30)

pilha.desempilhar()

pilha.percorrer()