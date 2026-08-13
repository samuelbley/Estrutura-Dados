# Crie uma classe chamada Aluno que armazene as seguintes informações:
# nome do aluno e uma lista com três notas.
# Em seguida, instancie três objetos da classe com nomes e notas diferentes 
# e armazene-os em uma lista chamada turma.
# Por fim, percorra a lista e exiba, para cada aluno, o nome e a média 
# das três notas.

class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)

aluno1 = Aluno("Lucas", [8.0, 7.5, 9.0])
aluno2 = Aluno("Mariana", [5.0, 6.0, 4.5])
aluno3 = Aluno("Beatriz", [9.5, 8.5, 10.0])

turma = [aluno1, aluno2, aluno3]

for aluno in turma:
    media = aluno.calcular_media()
    print(aluno.nome, "- Média:", round(media, 2))
