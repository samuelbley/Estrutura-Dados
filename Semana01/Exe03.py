# Crie uma classe chamada Contato que armazene as seguintes 
# informações: nome, telefone e e-mail.
# Em seguida, instancie três objetos da classe 
# e armazene-os em uma lista chamada agenda.
# Por fim, percorra a lista e exiba o nome e o telefone de cada contato.

class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

contato1 = Contato("Samuel Bley", "(55) 996436060", "samuel@gmail.com")
contato2 = Contato("Anelise Bley", "(55) 996172332", "anelise@gmail.com")
contato3 = Contato("Gleidson Toniasso", "(55) 999351834", "gleidson@gamil.com")

agenda = []
agenda.append(contato1)
agenda.append(contato2)
agenda.append(contato3)

for c in agenda:
    print(c.nome)
    print(c.telefone)