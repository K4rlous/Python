"Compreensões de Listas (List Comprehensions) são uma maneira concisa e eficiente de criar listas em Python. Elas permitem gerar uma nova lista aplicando uma expressão a cada item de uma sequência existente."

# Perceba que aplicamos condições dentro de compreensões de listas, economizando tempo e código!

"Exemplo Simples: Criar uma lista de quadrados dos números de 0 a 9."
quadrados = [x**2 for x in range(10)]
print(quadrados)  # Saída: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81] / Elevação ao quadrado!

"Com Condição: Incluir apenas números pares de 0 a 9."
pares = [x for x in range(10) if x % 2 == 0]
print(pares)  # Saída: [0, 2, 4, 6, 8]

"Convertendo Strings: Transformar caracteres em maiúsculas."
palavra = "python"
maiusculas = [char.upper() for char in palavra]
print(maiusculas)  # Saída: ['P', 'Y', 'T', 'H', 'O', 'N']

"Multiplicando Elementos: Multiplicar cada elemento de uma lista por 2."
numeros = [1, 2, 3, 4, 5]
dobros = [x * 2 for x in numeros]
print(dobros)  # Saída: [2, 4, 6, 8, 10]

"Usando Funções: Aplicar uma função a cada item da lista."
def inverter(s):
    return s[::-1]

palavras = ["abc", "def", "ghi"]
invertidas = [inverter(palavra) for palavra in palavras]
print(invertidas)  # Saída: ['cba', 'fed', 'ihg']

"O [::-1] em Python é uma técnica de fatiamento usada para inverter uma sequência, como uma string. A sintaxe s[start:stop:step] define os parâmetros de fatiamento: start é o índice inicial, stop é o índice final, e step é o incremento. Ao usar [::-1], start e stop não são especificados, então toda a sequência é considerada, e step é -1, o que percorre a sequência de trás para frente, resultando na inversão da string. "
