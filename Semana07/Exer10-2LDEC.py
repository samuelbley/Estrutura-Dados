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

    def adicionar_final(self, dado):
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

    def percorrer_frente(self, quantidade):
        if self.inicio is None:
            return

        aux = self.inicio

        for i in range(quantidade):
            print(aux.dado)
            aux = aux.proximo


lista = ListaDuplamenteEncadeadaCircular()

lista.adicionar_inicio(20)
lista.adicionar_inicio(10)

lista.adicionar_final(30)
lista.adicionar_final(40)

lista.percorrer_frente(7)