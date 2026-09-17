# FILA Simular uma sala de partidas em que jogadores entram numa fila. 
# A cada rodada, o jogador da frente participa da partida e volta 
# para o fim da fila, mantendo o rodízio contínuo.

# Adicionar jogador ao final da fila
# Simular 1 rodada (o primeiro joga e vai para o fim)
# Simular N rodadas (executa o item 3 repetido N vezes, exibindo a ordem a cada rodada)
# Mostrar fila (da posição 1 → fim)
# Mostrar próximo a jogar (frente da fila)
# Limpar fila
# Sair

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.proximo = None
        self.anterior = None

def menu():
    print("\n1 - Inserir jogador")
    print("2 - Simular 1 rodada")
    print("3 - Simular Nº rodadas")
    print("4 - Mostrar fila")
    print("5 - Mostrar próximo da fila")
    print("6 - Limpar Fila")
    print("7 - Sair")
    opc = int(input("Digite a opção desejada: "))
    return opc

def inserir_jogador(fila_inicio, fila_fim, nome):
    novo = Jogador(nome)
    if fila_inicio == None:
        fila_inicio = novo
        fila_fim = novo
        return fila_inicio, fila_fim

    novo.anterior = fila_fim
    fila_fim.proximo = novo
    fila_fim = novo
    return fila_inicio, fila_fim

def simular_uma_rodada(fila_inicio, fila_fim):
    if fila_inicio == None:
        print("Fila de jogadores Vazia")
        return fila_inicio, fila_fim

    if fila_inicio == fila_fim:
        print("Última rodada")
        print("Jogador", fila_inicio.nome)
        return fila_inicio, fila_fim

    print("Jogador jogando: ", fila_inicio.nome)
    fila_fim.proximo = fila_inicio
    fila_inicio.anterior = fila_fim
    fila_inicio = fila_inicio.proximo
    fila_fim = fila_inicio.anterior
    fila_inicio.anterior = None
    fila_fim.proximo = None
    return fila_inicio, fila_fim

def simular_n_rodadas(fila_inicio, fila_fim):
     if fila_inicio == None:
        print("Fila de jogadores vazia, insira jogadores na fila.")
        return fila_inicio, fila_fim

     rodadas = int(input("Quantas rodadas você deseja simular? "))
     if rodadas != 0:
        if fila_inicio == fila_fim:
                print("Só há um jogador, uma única rodada será simulada")
                print("Jogador", fila_inicio.nome)
                return fila_inicio, fila_fim
        print(f"Executando {rodadas} rodadas")
        for i in range(rodadas):
            print(f"{i+1}ª Rodada | Jogador: ",fila_inicio.nome)
            fila_fim.proximo = fila_inicio
            fila_inicio.anterior = fila_fim
            fila_inicio = fila_inicio.proximo
            fila_fim = fila_inicio.anterior
            fila_inicio.anterior = None
            fila_fim.proximo = None
        return fila_inicio, fila_fim
     else:
         print("Não mudou a fila, nenhuma rodada simulada")

def mostrar_fila(fila_inicio):
     aux = fila_inicio
     contador = 1
     

     if fila_inicio == None:
          print("Fila de jogadores vazia!")
          return
     
     while aux != None:
          print(contador, "-", aux.nome)
          contador+=1
          aux = aux.proximo
     return

def mostra_proximo_da_fila(fila_inicio):
     aux = fila_inicio
     if fila_inicio == None:
          print("A fila está vazia")
          return
     if fila_inicio.proximo == None:
          print("Não há nenhum depois")
          return
     print(f"O próximo da fila é: ", fila_inicio.proximo.nome)
     return

def limpar_fila(fila_inicio, fila_fim):
     if fila_inicio == None:
        print("Fila de jogadores vazia!")
        return fila_inicio, fila_fim

     print("Fila de jogadores foi limpa!")
     fila_inicio = None
     fila_fim = None
     return fila_inicio, fila_fim

def main():
    opcao = 0
    fila_inicio = None
    fila_fim = None
    

    while opcao != 7:
         opcao = menu()
         if opcao == 1:
              nome = str(input("Digite o nome do jogador: "))
              fila_inicio, fila_fim = inserir_jogador(fila_inicio, fila_fim, nome)
         elif opcao == 2:
              fila_inicio, fila_fim = simular_uma_rodada(fila_inicio, fila_fim)
         elif opcao == 3:
              fila_inicio, fila_fim = simular_n_rodadas(fila_inicio, fila_fim)
         elif opcao == 4: 
              mostrar_fila(fila_inicio)
         elif opcao == 5:
              mostra_proximo_da_fila(fila_inicio)
         elif opcao == 6:
              fila_inicio, fila_fim = limpar_fila(fila_inicio, fila_fim)
main()
    
        