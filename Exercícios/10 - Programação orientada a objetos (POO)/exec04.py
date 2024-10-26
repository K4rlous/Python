# Abstração 

"Abstração é outro conceito fundamental da Programação Orientada a Objetos (POO), que se concentra em mostrar apenas os detalhes essenciais de um objeto, ocultando a complexidade. Pense na abstração como um jeito de simplificar e organizar as coisas, mostrando o que é necessário para a interação com o objeto, sem expor toda a sua complexidade interna."

"Quando você herda de uma classe abstrata, você é obrigado a implementar todos os métodos abstratos definidos na classe base. Esses métodos são 'contratos' que a classe filha deve cumprir, garantindo que ela forneça implementações específicas para esses métodos. Isso é essencial para manter a consistência e a funcionalidade esperada."

# Importação de Biblioteca (veremos isso logo mais!)
from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

class Carro(Veiculo):
    def ligar(self):
        print("O carro está ligando!")

    def desligar(self):
        print("O carro está desligando!")

    def dirigir(self):
        print("Dirigindo o carro!")

"Note que acima obrigatóriamente tivemos de herdar todos os métodos da classe pai 'Veiculo', mas isso não impede-nos de criar nossos proprios métodos!"

meucarro = Carro()
meucarro.ligar() # Saida: O carro está ligando!
meucarro.dirigir() # Saida: Dirigindo o carro!
meucarro.desligar() # Saida: O carro está desligando!