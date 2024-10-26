# Criação e manipulação de classes e objetos

"Classe: Uma estrutura que define atributos (dados) e métodos (funções) que representam um objeto específico. Objeto: Uma instância de uma classe. Construtor __init__: Método especial que inicializa os atributos de um objeto quando ele é criado. Atributos: Variáveis que pertencem a uma classe ou instância. Métodos: Funções que pertencem a uma classe ou instância."

"Classe"

# Nome da classe
class Pessoa:

    # Métodos:

     # Método construtor (__init__) para inicializar os atributos da classe
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Método para mostrar informações do objeto
    def mostrarinfo(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")
    
    # Método para verificar se a pessoa é maior de idade
    def mais18(self):
        return self.idade >= 18
    
"Criação de Objetos"

pessoa1 = Pessoa('Ana', 19)
pessoa2 = Pessoa('Beatriz', 21)
pessoa3 = Pessoa('Carlos', 23)

"Acessando Atributos e Métodos"

# Atributos
print(pessoa1.nome) # Saida: 'Ana'
print(pessoa2.idade) # Saida: 21
print(pessoa3.nome) # Saida: 'Carlos'

# Métodos
pessoa1.mostrarinfo() # Saida: Nome: Ana, Idade: 19
pessoa3.mostrarinfo() # Saida: Nome: Carlos, Idade: 23
print(pessoa2.mais18()) # Saida: True
        