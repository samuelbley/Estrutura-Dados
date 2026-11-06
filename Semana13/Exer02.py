# Crie uma função recursiva chamada contagem_regressiva que 
# receba um número inteiro positivo como parâmetro e apresente 
# uma contagem regressiva até zero.
# Ao chegar em zero, a função deve exibir a mensagem:
# Viagem no tempo iniciada!

# Se o usuário informar: 5
# A saída deverá ser:
#      5
#      4
#      3
#      2
#      1
#      0
# Viagem no tempo iniciada!

def contagem_regressiva(num):
    if num == 0:
        print(" "*10,0)
        print("Viagen no tempo iniciada!\n")
    else:
        print(" "*10,num)
        contagem_regressiva(num - 1)

def main():
    opc = 0

    while opc != 2:
        print("1 - Iniciar contagem regressiva")
        print("2 - Sair")

        opc = int(input("Escolha uma opção: "))

        if opc == 1:
            num = int(input("Em qual número deseja iniciar a contagem? "))
            contagem_regressiva(num)
        elif opc == 2:
            print("SAINDO")
        else:
            print("Opção inválida!")

main()