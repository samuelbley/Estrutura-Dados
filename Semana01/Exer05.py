# Crie uma classe Livro com os atributos: título, autor e número de páginas.
# Implemente um método que informe se o livro é "curto" ou "longo", considerando:
# até 100 páginas = curto
# mais de 100 páginas = longo

# Crie dois objetos e mostre o resultado do método para cada um.

class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def verificar_tamanho(self):
        if self.paginas <= 100:
            return "curto"
        else:
            return "longo"

livro1 = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 96)
livro2 = Livro("Dom Casmurro", "Machado de Assis", 256)

print(livro1.titulo, "-", livro1.verificar_tamanho())
print(livro2.titulo, "-", livro2.verificar_tamanho())