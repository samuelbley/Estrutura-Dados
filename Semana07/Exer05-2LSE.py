class No:
    def __init__(self, nome):
        self.nome = nome
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.inicio = None

    def adicionar_inicio(self, nome):
        novo = No(nome)
        novo.proximo = self.inicio
        self.inicio = novo

    def adicionar_final(self, nome):
        novo = No(nome)

        if self.inicio is None:
            self.inicio = novo
        else:
            aux = self.inicio

            while aux.proximo is not None:
                aux = aux.proximo

            aux.proximo = novo

    def percorrer(self):
        aux = self.inicio

        while aux is not None:
            print(aux.nome)
            aux = aux.proximo


lista = ListaEncadeada()

lista.adicionar_inicio("João")
lista.adicionar_inicio("Pedro")
lista.adicionar_final("Carlos")
lista.adicionar_final("Lucas")

lista.percorrer()