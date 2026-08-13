# Crie uma classe Funcionario com os atributos: nome, salário e cargo.
# Implemente um método calcular_bonus() que retorne:
# 10% de bônus para o cargo "Gerente"
# 5% de bônus para os demais cargos

# Instancie dois funcionários e exiba o salário com bônus de cada um.

class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def calcular_bonus(self):
        if self.cargo == "Gerente":
            return self.salario * 0.10
        else:
            return self.salario * 0.05

funcionario1 = Funcionario("Carlos", 8000.00, "Gerente")
funcionario2 = Funcionario("Ana", 3000.00, "Analista")

total_f1 = funcionario1.salario + funcionario1.calcular_bonus()
total_f2 = funcionario2.salario + funcionario2.calcular_bonus()

print(funcionario1.nome, "- Cargo:", funcionario1.cargo, "- Salário com bônus:", total_f1)
print(funcionario2.nome, "- Cargo:", funcionario2.cargo, "- Salário com bônus:", total_f2)