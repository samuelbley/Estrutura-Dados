# Crie uma classe Pessoa com atributos nome e idade. 
# Implemente um método apresentar() que imprima uma mensagem com o nome e a idade da pessoa. 
# Crie dois objetos da classe Pessoa e chame o método apresentar() para cada um.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")


pessoa1 = Pessoa("Samuel", 19)
pessoa2 = Pessoa("João", 20)

pessoa1.apresentar()
pessoa2.apresentar()