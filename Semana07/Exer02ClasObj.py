# Desenvolva uma classe Retangulo com atributos largura e altura. 
# Adicione métodos para calcular a area() e o perimetro() do retângulo. 
# Crie um objeto Retangulo e exiba seus cálculos.

class Retangulo: 
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        area = self.largura * self.altura
        print("Área = ", area)

    def calcular_perimetro(self):
        perimetro = (self.altura+self.altura)+(self.largura+self.largura)
        print("Perímetro = ", perimetro)

retangulo1 = Retangulo(10,30)

retangulo1.calcular_area()
retangulo1.calcular_perimetro()
