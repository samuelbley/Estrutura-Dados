# Uma função recursiva realiza a soma dos números 
# inteiros de 1 até \(n\), seguindo a regra:
# soma(1)=1
# soma(n)=n+soma(n-1)
# Mostre a sequência de chamadas e retornos para soma(6).

def soma(n):
    print(f"Chamando soma({n})")

    if n == 1:
        return 1
    else:
        resultado = n + soma(n - 1)
        return resultado


def main():
    num = 6
    resultado = soma(num)

    print(f"\nResultado final: {resultado}")


main()