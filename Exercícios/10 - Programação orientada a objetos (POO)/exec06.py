# Argumentos Variáveis

"Em Python, você pode usar argumentos variáveis para permitir que uma função aceite um número indefinido de argumentos. Isso é feito usando *args para argumentos posicionais e **kwargs para argumentos nomeados. Isso dá muita flexibilidade na hora de definir funções."

"Argumentos Posicionais Variáveis (*args): Permite que a função receba um número variável de argumentos, que são empacotados em uma tupla."

class Calculadora:
    # Note que usamos *args no lugar de argumentos adicionais 
    def somar(self, *args):
        # Sum = soma :)
        return sum(args)

calc = Calculadora()
print(calc.somar(1, 2))    # Saída: 3
print(calc.somar(1, 2, 3)) # Saída: 6
print(calc.somar(1, 2, 3, 4)) # Saída: 10


def somar(*args):
    return sum(args)

print(somar(1, 2, 3))          # Saída: 6
print(somar(1, 2, 3, 4, 5))    # Saída: 15

"Argumentos Nomeados Variáveis (**kwargs): Permite que a função receba um número variável de argumentos nomeados, que são empacotados em um dicionário."

def exibir_info(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

exibir_info(nome="Alice", idade=30)  
# Saída:
# nome: Alice
# idade: 30

exibir_info(cidade="São Paulo", país="Brasil")  
# Saída:
# cidade: São Paulo
# país: Brasil

"Combinação de *args e **kwargs: Você também pode combinar os dois para aceitar ambos os tipos de argumentos na mesma função."

def combinar(*args, **kwargs):
    for arg in args:
        print(f"Arg: {arg}")
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

combinar(1, 2, 3, nome="Alice", idade=30)  
# Saída:
# Arg: 1
# Arg: 2
# Arg: 3
# nome: Alice
# idade: 30
