# Durante a preparação para uma partida de futebol, o treinador 
# precisa organizar os jogadores em uma lista. Implemente uma lista 
# simplesmente encadeada em Python para representar essa escalação. 
# Crie uma classe No para representar cada jogador, contendo o nome 
# do jogador e a referência para o proximo jogador da lista. Em seguida, 
# crie a classe ListaEncadeada com os métodos adicionar_inicio(nome) 
# e percorrer(). Adicione alguns jogadores ao início da lista e apresente, 
# ao final, todos os jogadores cadastrados.

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.proximo = None

def inserir_jogador(fila, nome):
    novo = Jogador(nome)

    if fila is None:
        fila = novo
        return fila

    novo.proximo = fila
    fila = novo
    return fila

def mostrar_escalacao(fila):
    aux = fila
    contador = 1

    if fila is None:
        print("Sem jogadores na escalação")
        return

    while aux != None:
        print(f"\n{contador} - {aux.nome}")
        contador+=1
        aux = aux.proximo

def main():
    fila = None
    opc = 0

    while opc != 3:
        print("1 - INSERIR")
        print("2 - ESCALAÇÃO")
        opc = int(input("Digite a opção: "))

        if opc == 1:
            nome = str(input("Qual é o nome do jogador? "))
            fila = inserir_jogador(fila, nome)
        elif opc == 2:
            mostrar_escalacao(fila)

main()