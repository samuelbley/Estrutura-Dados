<<<<<<< HEAD
class No:
    def __init__(self, matricula, nome, situacao=True, nota_final=0.0):
        self.matricula = matricula
        self.nome = nome
        self.situacao = situacao
        self.nota_final = nota_final
        self.proximo = None


class ListaSimplesmenteEncadeada:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.quantidade = 0

    def cadastrar_aluno(self):
        matricula = int(input("Matrícula: "))
        nome = input("Nome: ")
        nota = float(input("Nota final: "))

        novo = No(matricula, nome, True, nota)

        if self.inicio is None:
            self.inicio = novo
            self.fim = novo
        else:
            self.fim.proximo = novo
            self.fim = novo

        self.quantidade += 1
        print("Aluno cadastrado com sucesso.")

    def listar_todos(self):
        if self.inicio is None:
            print("Nenhum aluno cadastrado.")
            return

        atual = self.inicio

        while atual:
            print(f"Matrícula: {atual.matricula}")
            print(f"Nome: {atual.nome}")
            print(f"Situação: {'Ativo' if atual.situacao else 'Desativado'}")
            print(f"Nota final: {atual.nota_final:.2f}")
            print("-" * 30)
            atual = atual.proximo

    def listar_ativos(self):
        atual = self.inicio
        encontrou = False

        while atual:
            if atual.situacao:
                encontrou = True
                print(f"Matrícula: {atual.matricula}")
                print(f"Nome: {atual.nome}")
                print(f"Situação: Ativo")
                print(f"Nota final: {atual.nota_final:.2f}")
                print("-" * 30)
            atual = atual.proximo

        if not encontrou:
            print("Nenhum aluno ativo.")

    def listar_desativados(self):
        atual = self.inicio
        encontrou = False

        while atual:
            if not atual.situacao:
                encontrou = True
                print(f"Matrícula: {atual.matricula}")
                print(f"Nome: {atual.nome}")
                print(f"Situação: Desativado")
                print(f"Nota final: {atual.nota_final:.2f}")
                print("-" * 30)
            atual = atual.proximo

        if not encontrou:
            print("Nenhum aluno desativado.")

    def buscar_aluno(self):
        matricula = int(input("Informe a matrícula: "))
        atual = self.inicio

        while atual:
            if atual.matricula == matricula:
                print(f"Matrícula: {atual.matricula}")
                print(f"Nome: {atual.nome}")
                print(f"Situação: {'Ativo' if atual.situacao else 'Desativado'}")
                print(f"Nota final: {atual.nota_final:.2f}")
                return
            atual = atual.proximo

        print("Aluno não encontrado.")

    def alterar_nota(self):
        matricula = int(input("Informe a matrícula: "))
        atual = self.inicio

        while atual:
            if atual.matricula == matricula:
                atual.nota_final = float(input("Nova nota final: "))
                print("Nota alterada com sucesso.")
                return
            atual = atual.proximo

        print("Aluno não encontrado.")

    def alterar_situacao(self):
        matricula = int(input("Informe a matrícula: "))
        atual = self.inicio

        while atual:
            if atual.matricula == matricula:
                atual.situacao = not atual.situacao
                print("Situação alterada com sucesso.")
                return
            atual = atual.proximo

        print("Aluno não encontrado.")

    def remover_aluno(self):
        matricula = int(input("Informe a matrícula: "))

        atual = self.inicio
        anterior = None

        while atual:
            if atual.matricula == matricula:
                if anterior is None:
                    self.inicio = atual.proximo
                else:
                    anterior.proximo = atual.proximo

                if atual == self.fim:
                    self.fim = anterior

                self.quantidade -= 1
                print("Aluno removido com sucesso.")
                return

            anterior = atual
            atual = atual.proximo

        print("Aluno não encontrado.")

    def informar_quantidade(self):
        print(f"Quantidade de alunos cadastrados: {self.quantidade}")

    def media_turma(self):
        if self.inicio is None:
            print("Nenhum aluno cadastrado.")
            return

        soma = 0
        atual = self.inicio

        while atual:
            soma += atual.nota_final
            atual = atual.proximo

        media = soma / self.quantidade
        print(f"Média da turma: {media:.2f}")

    def media_ativos(self):
        atual = self.inicio
        soma = 0
        quantidade = 0

        while atual:
            if atual.situacao:
                soma += atual.nota_final
                quantidade += 1
            atual = atual.proximo

        if quantidade == 0:
            print("Nenhum aluno ativo.")
            return

        media = soma / quantidade
        print(f"Média dos alunos ativos: {media:.2f}")


lista = ListaSimplesmenteEncadeada()

while True:
    print("\n1 - Cadastrar aluno")
    print("2 - Listar todos os alunos")
    print("3 - Listar alunos ativos")
    print("4 - Listar alunos desativados")
    print("5 - Buscar aluno pela matrícula")
    print("6 - Alterar nota final")
    print("7 - Alterar situação")
    print("8 - Remover aluno")
    print("9 - Quantidade de alunos")
    print("10 - Média da turma")
    print("11 - Média dos alunos ativos")
    print("0 - Sair")

    opcao = int(input("Escolha: "))

    if opcao == 1:
        lista.cadastrar_aluno()
    elif opcao == 2:
        lista.listar_todos()
    elif opcao == 3:
        lista.listar_ativos()
    elif opcao == 4:
        lista.listar_desativados()
    elif opcao == 5:
        lista.buscar_aluno()
    elif opcao == 6:
        lista.alterar_nota()
    elif opcao == 7:
        lista.alterar_situacao()
    elif opcao == 8:
        lista.remover_aluno()
    elif opcao == 9:
        lista.informar_quantidade()
    elif opcao == 10:
        lista.media_turma()
    elif opcao == 11:
        lista.media_ativos()
    elif opcao == 0:
        break
    else:
=======
class No:
    def __init__(self, matricula, nome, situacao=True, nota_final=0.0):
        self.matricula = matricula
        self.nome = nome
        self.situacao = situacao
        self.nota_final = nota_final
        self.proximo = None


class ListaSimplesmenteEncadeada:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.quantidade = 0

    def cadastrar_aluno(self):
        matricula = int(input("Matrícula: "))
        nome = input("Nome: ")
        nota = float(input("Nota final: "))

        novo = No(matricula, nome, True, nota)

        if self.inicio is None:
            self.inicio = novo
            self.fim = novo
        else:
            self.fim.proximo = novo
            self.fim = novo

        self.quantidade += 1
        print("Aluno cadastrado com sucesso.")

    def listar_todos(self):
        if self.inicio is None:
            print("Nenhum aluno cadastrado.")
            return

        atual = self.inicio

        while atual:
            print(f"Matrícula: {atual.matricula}")
            print(f"Nome: {atual.nome}")
            print(f"Situação: {'Ativo' if atual.situacao else 'Desativado'}")
            print(f"Nota final: {atual.nota_final:.2f}")
            print("-" * 30)
            atual = atual.proximo

    def listar_ativos(self):
        atual = self.inicio
        encontrou = False

        while atual:
            if atual.situacao:
                encontrou = True
                print(f"Matrícula: {atual.matricula}")
                print(f"Nome: {atual.nome}")
                print(f"Situação: Ativo")
                print(f"Nota final: {atual.nota_final:.2f}")
                print("-" * 30)
            atual = atual.proximo

        if not encontrou:
            print("Nenhum aluno ativo.")

    def listar_desativados(self):
        atual = self.inicio
        encontrou = False

        while atual:
            if not atual.situacao:
                encontrou = True
                print(f"Matrícula: {atual.matricula}")
                print(f"Nome: {atual.nome}")
                print(f"Situação: Desativado")
                print(f"Nota final: {atual.nota_final:.2f}")
                print("-" * 30)
            atual = atual.proximo

        if not encontrou:
            print("Nenhum aluno desativado.")

    def buscar_aluno(self):
        matricula = int(input("Informe a matrícula: "))
        atual = self.inicio

        while atual:
            if atual.matricula == matricula:
                print(f"Matrícula: {atual.matricula}")
                print(f"Nome: {atual.nome}")
                print(f"Situação: {'Ativo' if atual.situacao else 'Desativado'}")
                print(f"Nota final: {atual.nota_final:.2f}")
                return
            atual = atual.proximo

        print("Aluno não encontrado.")

    def alterar_nota(self):
        matricula = int(input("Informe a matrícula: "))
        atual = self.inicio

        while atual:
            if atual.matricula == matricula:
                atual.nota_final = float(input("Nova nota final: "))
                print("Nota alterada com sucesso.")
                return
            atual = atual.proximo

        print("Aluno não encontrado.")

    def alterar_situacao(self):
        matricula = int(input("Informe a matrícula: "))
        atual = self.inicio

        while atual:
            if atual.matricula == matricula:
                atual.situacao = not atual.situacao
                print("Situação alterada com sucesso.")
                return
            atual = atual.proximo

        print("Aluno não encontrado.")

    def remover_aluno(self):
        matricula = int(input("Informe a matrícula: "))

        atual = self.inicio
        anterior = None

        while atual:
            if atual.matricula == matricula:
                if anterior is None:
                    self.inicio = atual.proximo
                else:
                    anterior.proximo = atual.proximo

                if atual == self.fim:
                    self.fim = anterior

                self.quantidade -= 1
                print("Aluno removido com sucesso.")
                return

            anterior = atual
            atual = atual.proximo

        print("Aluno não encontrado.")

    def informar_quantidade(self):
        print(f"Quantidade de alunos cadastrados: {self.quantidade}")

    def media_turma(self):
        if self.inicio is None:
            print("Nenhum aluno cadastrado.")
            return

        soma = 0
        atual = self.inicio

        while atual:
            soma += atual.nota_final
            atual = atual.proximo

        media = soma / self.quantidade
        print(f"Média da turma: {media:.2f}")

    def media_ativos(self):
        atual = self.inicio
        soma = 0
        quantidade = 0

        while atual:
            if atual.situacao:
                soma += atual.nota_final
                quantidade += 1
            atual = atual.proximo

        if quantidade == 0:
            print("Nenhum aluno ativo.")
            return

        media = soma / quantidade
        print(f"Média dos alunos ativos: {media:.2f}")


lista = ListaSimplesmenteEncadeada()

while True:
    print("\n1 - Cadastrar aluno")
    print("2 - Listar todos os alunos")
    print("3 - Listar alunos ativos")
    print("4 - Listar alunos desativados")
    print("5 - Buscar aluno pela matrícula")
    print("6 - Alterar nota final")
    print("7 - Alterar situação")
    print("8 - Remover aluno")
    print("9 - Quantidade de alunos")
    print("10 - Média da turma")
    print("11 - Média dos alunos ativos")
    print("0 - Sair")

    opcao = int(input("Escolha: "))

    if opcao == 1:
        lista.cadastrar_aluno()
    elif opcao == 2:
        lista.listar_todos()
    elif opcao == 3:
        lista.listar_ativos()
    elif opcao == 4:
        lista.listar_desativados()
    elif opcao == 5:
        lista.buscar_aluno()
    elif opcao == 6:
        lista.alterar_nota()
    elif opcao == 7:
        lista.alterar_situacao()
    elif opcao == 8:
        lista.remover_aluno()
    elif opcao == 9:
        lista.informar_quantidade()
    elif opcao == 10:
        lista.media_turma()
    elif opcao == 11:
        lista.media_ativos()
    elif opcao == 0:
        break
    else:
>>>>>>> b8ffbb4f4b6e3adb9bb985b77ac8557328ba63c9
        print("Opção inválida.")