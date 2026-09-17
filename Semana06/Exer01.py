# FILA Implemente um sistema de atendimento de Suporte de TI utilizando 
# uma fila comum (FIFO). O sistema deve permitir registrar chamados 
# (nomes das pessoas) na ordem de chegada. Quando um atendimento 
# ocorre, o primeiro da fila é removido e seu nome é exibido. 
# O programa deve mostrar quantos chamados ainda aguardam e quem 
# é o próximo. Utilize as operações de inserção e remoção da fila 
# para gerenciar os atendimentos.

class Chamado:
    def __init__(self, nome):
        self.nome = nome
        self.proximo = None
        self.anterior = None 

def registrar_chamado(fila_inicio, fila_fim, nome):
    novo = Chamado(nome)
    if fila_inicio is None:
        fila_inicio = novo
        fila_fim = novo
        return fila_inicio, fila_fim

    fila_fim.proximo = novo
    novo.anterior = fila_fim
    fila_fim = novo
    return fila_inicio, fila_fim

def listar_chamados(fila_inicio):
    aux = fila_inicio
    contador = 1

    if fila_inicio == None:
        print("Fila vazia")
        return 
    
    while aux != None:
        print(contador, "-", aux.nome)
        contador+=1
        aux = aux.proximo

def resolver_chamado(fila_inicio, fila_fim):
    if fila_inicio == None:
        print("Fila vazia")
        return None, None
    
    if fila_inicio == fila_fim:
        print("Único elemento na fila")
        print("Chamado resolvido: ", fila_inicio.nome)
        print("Agora a fila está vazia")
        return None, None
    
    else:
        print("Chamado resolvido: ",fila_inicio.nome)
        fila_inicio = fila_inicio.proximo
        fila_inicio.anterior = None

        aux = fila_inicio
        contador = 0
        while aux != None:
            contador += 1
            aux = aux.proximo

        print(f"Restam {contador} chamado(s) na fila.")
        print(f"Próximo a ser atendido: {fila_inicio.nome}")
        return fila_inicio, fila_fim

def main():
    opcao = 0
    fila_inicio = None
    fila_fim = None
    while opcao!=4:
        print("======MENU======")
        print("1 - Registrar chamado (nome): ")
        print("2 - Listar chamados")
        print("3 - Resolver um chamado")
        print("4 - Sair")
        opcao = int(input("\nDigite a opção desejada: "))
        if opcao == 1:
            nome = str(input("Digite o nome do chamado: "))
            fila_inicio, fila_fim = registrar_chamado(fila_inicio, fila_fim, nome)
        elif opcao == 2:
            listar_chamados(fila_inicio)
        elif opcao == 3:
            fila_inicio, fila_fim = resolver_chamado(fila_inicio, fila_fim)
        elif opcao == 4:
            break
main()
    

