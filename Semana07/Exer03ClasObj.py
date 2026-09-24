# Crie uma classe Carro com atributos marca, modelo e ano. 
# Implemente um método ligar() que imprima "Carro ligado!" 
# e um método desligar() que imprima "Carro desligado!". 
# Crie um objeto Carro e demonstre o uso dos métodos.

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def ligar_carro(self):
        print(f"Seu {self.modelo} está ligado!")

    def desligar_carro(self):
        print(f"Seu {self.modelo} está desligado!")

carro1 = Carro("Fiat", "Uno", "2003")

carro1.ligar_carro()
carro1.desligar_carro()