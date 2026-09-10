class Paciente:
    def __init__(self, nome, idade, prioridade):
        self.nome = nome
        self.idade = idade
        self.prioridade = prioridade
        self.proximo = None
        self.anterior = None

    def inserir(self, nome, idade, prioridade):
        novo = Paciente(nome, idade, prioridade)

        ultimo = self.anterior

        ultimo.proximo = novo
        novo.anterior = ultimo
        novo.proximo = self
        self.anterior = novo

    def mostrar(self):
        atual = self

        while True:
            print(atual.nome, atual.idade, atual.prioridade)

            atual = atual.proximo

            if atual == self:
                break

    def contar(self):
        quantidade = 1
        atual = self.proximo

        while atual != self:
            quantidade += 1
            atual = atual.proximo

        return quantidade

    def remover(self, paciente):
        paciente.anterior.proximo = paciente.proximo
        paciente.proximo.anterior = paciente.anterior

    def buscar_prioridade(self, prioridade):
        atual = self

        while True:
            if atual.prioridade == prioridade:
                return atual

            atual = atual.proximo

            if atual == self:
                return None

    def atender(self):
        quantidade = self.contar()

        while quantidade > 0:
            paciente = self.buscar_prioridade("emergencia")

            if paciente is None:
                paciente = self.buscar_prioridade("urgente")

            if paciente is None:
                paciente = self.buscar_prioridade("normal")

            print("Atendendo:", paciente.nome)

            proximo = paciente.proximo

            self.remover(paciente)

            quantidade -= 1

            if quantidade > 0:
                paciente = proximo


def main():
    cabeca = Paciente("Carlos", 35, "normal")
    cabeca.proximo = cabeca
    cabeca.anterior = cabeca

    cabeca.inserir("Maria", 42, "urgente")
    cabeca.inserir("João", 28, "normal")
    cabeca.inserir("Ana", 55, "emergencia")
    cabeca.inserir("Pedro", 31, "urgente")

    print("Pacientes:")
    cabeca.mostrar()

    print()
    print("Atendimento:")

    cabeca.atender()


main()
