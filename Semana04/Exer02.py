class No:
    def __init__(self, codigo, nome, idade, prioridade):
        self.codigo = codigo
        self.nome = nome
        self.idade = idade
        self.prioridade = prioridade
        self.anterior = None
        self.proximo = None


class ListaDuplamenteEncadeada:
    prioridades = {
        "Emergência": 1,
        "Muito urgente": 2,
        "Urgente": 3,
        "Pouco urgente": 4,
        "Não urgente": 5
    }

    def __init__(self):
        self.inicio = None
        self.fim = None
        self.quantidade = 0

    def cadastrar_paciente(self):
        codigo = int(input("Código: "))
        nome = input("Nome: ")
        idade = int(input("Idade: "))

        print("1 - Emergência")
        print("2 - Muito urgente")
        print("3 - Urgente")
        print("4 - Pouco urgente")
        print("5 - Não urgente")

        opcao = int(input("Prioridade: "))

        prioridades = {
            1: "Emergência",
            2: "Muito urgente",
            3: "Urgente",
            4: "Pouco urgente",
            5: "Não urgente"
        }

        if opcao not in prioridades:
            print("Prioridade inválida.")
            return

        novo = No(codigo, nome, idade, prioridades[opcao])

        if self.inicio is None:
            self.inicio = novo
            self.fim = novo
        else:
            novo.anterior = self.fim
            self.fim.proximo = novo
            self.fim = novo

        self.quantidade += 1
        print("Paciente cadastrado com sucesso.")

    def remover_por_codigo(self, codigo):
        atual = self.inicio

        while atual:
            if atual.codigo == codigo:
                if atual.anterior:
                    atual.anterior.proximo = atual.proximo
                else:
                    self.inicio = atual.proximo

                if atual.proximo:
                    atual.proximo.anterior = atual.anterior
                else:
                    self.fim = atual.anterior

                self.quantidade -= 1
                return atual

            atual = atual.proximo

        return None

    def remover_paciente(self):
        codigo = int(input("Código do paciente a remover: "))
        paciente = self.remover_por_codigo(codigo)

        if paciente:
            print("Paciente removido com sucesso.")
        else:
            print("Paciente não encontrado.")

    def localizar_paciente(self):
        codigo = int(input("Código do paciente: "))
        atual = self.inicio

        while atual:
            if atual.codigo == codigo:
                print(f"Código: {atual.codigo}")
                print(f"Nome: {atual.nome}")
                print(f"Idade: {atual.idade}")
                print(f"Prioridade: {atual.prioridade}")
                return
            atual = atual.proximo

        print("Paciente não encontrado.")

    def atender_mais_urgente(self):
        if self.inicio is None:
            print("Nenhum paciente aguardando atendimento.")
            return

        atual = self.inicio
        mais_urgente = atual

        while atual:
            if self.prioridades[atual.prioridade] < self.prioridades[mais_urgente.prioridade]:
                mais_urgente = atual
            atual = atual.proximo

        paciente = self.remover_por_codigo(mais_urgente.codigo)

        print("Paciente atendido:")
        print(f"Código: {paciente.codigo}")
        print(f"Nome: {paciente.nome}")
        print(f"Idade: {paciente.idade}")
        print(f"Prioridade: {paciente.prioridade}")

    def listar_primeiro_ultimo(self):
        if self.inicio is None:
            print("Nenhum paciente aguardando atendimento.")
            return

        atual = self.inicio

        while atual:
            print(f"Código: {atual.codigo}")
            print(f"Nome: {atual.nome}")
            print(f"Idade: {atual.idade}")
            print(f"Prioridade: {atual.prioridade}")
            print("-" * 30)
            atual = atual.proximo

    def listar_por_prioridade(self):
        print("1 - Emergência")
        print("2 - Muito urgente")
        print("3 - Urgente")
        print("4 - Pouco urgente")
        print("5 - Não urgente")

        opcao = int(input("Escolha a prioridade: "))

        prioridades = {
            1: "Emergência",
            2: "Muito urgente",
            3: "Urgente",
            4: "Pouco urgente",
            5: "Não urgente"
        }

        if opcao not in prioridades:
            print("Prioridade inválida.")
            return

        prioridade = prioridades[opcao]
        atual = self.inicio
        encontrou = False

        while atual:
            if atual.prioridade == prioridade:
                encontrou = True
                print(f"Código: {atual.codigo}")
                print(f"Nome: {atual.nome}")
                print(f"Idade: {atual.idade}")
                print(f"Prioridade: {atual.prioridade}")
                print("-" * 30)
            atual = atual.proximo

        if not encontrou:
            print("Nenhum paciente possui essa prioridade.")

    def listar_ultimo_primeiro(self):
        if self.fim is None:
            print("Nenhum paciente aguardando atendimento.")
            return

        atual = self.fim

        while atual:
            print(f"Código: {atual.codigo}")
            print(f"Nome: {atual.nome}")
            print(f"Idade: {atual.idade}")
            print(f"Prioridade: {atual.prioridade}")
            print("-" * 30)
            atual = atual.anterior

    def quantidade_pacientes(self):
        print(f"Quantidade de pacientes aguardando atendimento: {self.quantidade}")


lista = ListaDuplamenteEncadeada()

while True:
    print("\n1 - Cadastrar paciente")
    print("2 - Remover paciente")
    print("3 - Localizar paciente pelo código")
    print("4 - Atender paciente mais urgente")
    print("5 - Listar do primeiro para o último")
    print("6 - Listar por prioridade")
    print("7 - Listar do último para o primeiro")
    print("8 - Quantidade de pacientes")
    print("0 - Sair")

    opcao = int(input("Escolha: "))

    if opcao == 1:
        lista.cadastrar_paciente()
    elif opcao == 2:
        lista.remover_paciente()
    elif opcao == 3:
        lista.localizar_paciente()
    elif opcao == 4:
        lista.atender_mais_urgente()
    elif opcao == 5:
        lista.listar_primeiro_ultimo()
    elif opcao == 6:
        lista.listar_por_prioridade()
    elif opcao == 7:
        lista.listar_ultimo_primeiro()
    elif opcao == 8:
        lista.quantidade_pacientes()
    elif opcao == 0:
        break
    else:
        print("Opção inválida.")