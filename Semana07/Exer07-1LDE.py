class NoDuplo:
    def __init__(self, nome):
        self.nome = nome
        self.anterior = None
        self.proximo = None


class ListaDuplamenteEncadeada:
    def __init__(self):
        self.inicio = None

    def adicionar_inicio(self, nome):
        novo = NoDuplo(nome)

        if self.inicio is not None:
            novo.proximo = self.inicio
            self.inicio.anterior = novo

        self.inicio = novo

    def percorrer_frente(self):
        aux = self.inicio

        while aux is not None:
            print(aux.nome)
            aux = aux.proximo


lista = ListaDuplamenteEncadeada()

lista.adicionar_inicio("João")
lista.adicionar_inicio("Pedro")
lista.adicionar_inicio("Carlos")

lista.percorrer_frente()