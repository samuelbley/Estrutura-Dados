# Faça um algoritmo que utilize lista duplamente encadeada 
# para armazenar informações de alunos. Cada nó deve conter:
# Identificador (ID)
# Nome do aluno
# Nota final
# O algoritmo deve apresentar o seguinte menu principal:
# Inserir aluno
# Listar alunos
# Remover aluno
# Mostrar situação dos alunos
# Listar todos os alunos classificados como:
# Aprovado (nota ≥ 7,0)
# Exame (nota entre 4,0 e 6,9)
# Reprovado (nota < 4,0)
# Sair

class Alunos: 
    def __init__(self, id, nome, nota):
        self.id = id
        self.nome = nome
        self.note = nota
        self.anterior = None
        self.proximo = None

def menu():
    print("1- Inserir Aluno")
    print("2- Listar Alunos")
    print("3- Remover Aluno")
    print("4- Mostrar Situação")
    print("5- Listar Aprovados/Reprovados/Exame")
    opcao = int(input("Opção: "))
    return opcao 

def inserir_aluno(lista, id, nome, nota):
    print("="*5,"INSERIR ALUNO","="*5)
    id = int(input("Digite o ID: "))
    nome = str(input("Digite o Nome: "))
    nota = float(input("Digite a Nota"))
    novo = Alunos(id, nome, nota)
    if lista is None:
        lista = novo
        return lista

    novo.proximo = lista
    lista.anterior = novo
    lista = novo 
    return lista

def listar_alunos(lista):
    copia_lista = lista

    while copia_lista != None:
        print("ALUNO: ", copia_lista.nome)

        copia_lista = copia_lista.proximo

def remover_aluno(lista,id):

def main():
    lista = None
    opcao = 0
    
 main()
