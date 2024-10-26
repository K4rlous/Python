# Conceitos de Herança e Polimorfismo

"Herança: Herança permite criar uma nova classe (classe filha) baseada em uma classe existente (classe pai), herdando seus atributos e métodos. Isso promove reutilização de código e facilita a manutenção, mas perceba que não somos obrigados a implementar todos os métodos herdados, essa caracteristica só se apresenta no conceito de abstração."
class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def fazersom(self):
        pass # Esse método não retorna nada, simplesmente 'passe'

# Note que colocamos o nome da classe que queremos herdar entre ()
class Cachorro(Animal):
    def fazersom(self): # Perceba que fazemos alterações no método herdado
        return 'Au, Au'


class Gato(Animal):
    def fazersom(self):
        return 'Miau, Miau'
    
"Agora vamos criar objetos e instânciar nomes para eles:"

cachorro = Cachorro('Beethoven')
gato = Gato('Gaspar')

print(cachorro.nome, cachorro.fazersom()) # Saida: Beethoven Au, Au
print(gato.nome, gato.fazersom()) # Saida: Gaspar Miau, Miau


"Polimorfismo: Polimorfismo permite que métodos com o mesmo nome em diferentes classes tenham comportamentos diferentes. Essencial para permitir que um objeto se comporte de diferentes maneiras dependendo do contexto."

'SIM. Eu sei que esse método está fora do escopo da classe :)'
# Função que aceita um objeto Animal
def imprimir_som(animal):
    print(animal.fazer_som())


# Usando Polimorfismo
imprimir_som(cachorro)  # Saída: Au Au
imprimir_som(gato)  # Saída: Miau