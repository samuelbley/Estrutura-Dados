class No:
    def __init__(self, nome, gols):
        self.nome = nome
        self.gols = gols
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.inicio = None

    def adicionar_inicio(self, nome, gols):
        novo = No(nome, gols)
        novo.proximo = self.inicio
        self.inicio = novo

    def adicionar_final(self, nome, gols):
        novo = No(nome, gols)

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
            print(aux.nome, "-", aux.gols, "gols")
            aux = aux.proximo

    def media_gols(self):
        aux = self.inicio
        total = 0
        quantidade = 0

        while aux is not None:
            total += aux.gols
            quantidade += 1
            aux = aux.proximo

        if quantidade == 0:
            return 0

        return total / quantidade


lista = ListaEncadeada()

lista.adicionar_inicio("João", 5)
lista.adicionar_inicio("Pedro", 8)
lista.adicionar_final("Carlos", 3)
lista.adicionar_final("Lucas", 6)

lista.percorrer()

print("Média de gols:", lista.media_gols())