# Sobrecarga de métodos 

"Em Python, não existe sobrecarga de métodos nativa como em Java, mas você pode usar argumentos padrão e argumentos variáveis para conseguir resultados semelhantes."

class Calculadora:
    def somar(self, a, b, c=0):
        return a + b + c

calc = Calculadora()
print(calc.somar(1, 2))    # Saída: 3
print(calc.somar(1, 2, 3)) # Saída: 6

class Ola:
    def saudar(self, nome="Usuário"):
        # Se um nome for fornecido pelo usuário, use-o, senão mantenha "Usuário"
        if nome == "Usuário":
            print(f"Olá, {nome}")
        else:
            print(f"Olá, {nome}")

# Criando uma instância de Ola
ola = Ola()

# Chamada sem parâmetro, deve resultar "Olá, Usuário"
ola.saudar()

# Chamada com parâmetro, deve resultar "Olá, NomeInserido"
nome = input("Qual o seu nome?  ")
ola.saudar(nome)
