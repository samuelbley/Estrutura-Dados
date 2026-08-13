# Crie uma classe Aluno que receba nome e uma lista com três notas.
# Implemente um método calcular_media() que retorne a média das notas.
# Implemente também um método verificar_aprovacao(), que retorne "Aprovado" 
# se a média for maior ou igual a 7, ou "Reprovado" caso contrário.
# Teste a classe com dois alunos e mostre os resultados.

class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)

    def verificar_aprovacao(self):
        if self.calcular_media() >= 7:
            return "Aprovado"
        else:
            return "Reprovado"

aluno1 = Aluno("Lucas", [8.0, 7.5, 9.0])
aluno2 = Aluno("Mariana", [5.0, 6.0, 4.5])

media1 = aluno1.calcular_media()
media2 = aluno2.calcular_media()

print(aluno1.nome, "- Média:", media1, "- Status:", aluno1.verificar_aprovacao())
print(aluno2.nome, "- Média:", round(media2, 2), "- Status:", aluno2.verificar_aprovacao())
