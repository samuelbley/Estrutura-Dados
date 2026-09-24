class NoDuploCircular:
    def __init__(self, dado):
        self.dado = dado
        self.anterior = None
        self.proximo = None


class ListaDuplamenteEncadeadaCircular:
    def __init__(self):
        self.inicio = None

    def adicionar_inicio(self, dado):
        novo = NoDuploCircular(dado)

        if self.inicio is None:
            novo.proximo = novo
            novo.anterior = novo
            self.inicio = novo
        else:
            ultimo = self.inicio.anterior

            novo.proximo = self.inicio
            novo.anterior = ultimo

            ultimo.proximo = novo
            self.inicio.anterior = novo

            self.inicio = novo

    def percorrer(self):
        if self.inicio is None:
            return

        aux = self.inicio

        while True:
            print(aux.dado)
            aux = aux.proximo

            if aux == self.inicio:
                break


lista = ListaDuplamenteEncadeadaCircular()

lista.adicionar_inicio(10)
lista.adicionar_inicio(20)
lista.adicionar_inicio(30)

lista.percorrer()