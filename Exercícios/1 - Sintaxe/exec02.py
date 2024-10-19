# Tipos de dados

# Inteiro (int)
"O tipo inteiro é um tipo composto por caracteres numéricos (algarismos) inteiros."
int = 1

# Ponto Flutuante ou Decimal (float)
"É um tipo composto por caracteres numéricos (algarismo) decimais."
float = 1.80 

# String (str)
"É um conjunto de caracteres dispostos numa determinada ordem, geralmente utilizada para representar palavras, frases ou textos."
string = "Python"

# Boolean (bool)
"Tipo de dado lógico que pode assumir apenas dois valores: falso ou verdadeiro (False ou True em Python)."
bool = False

# List (list)
"Listas agrupam um conjunto de elementos variados, podendo conter: inteiros, floats, strings, outras listas e outros tipos."
list1 = [1,2,3,4]
list2 = ["Carlos", "Ana", "Miguel" "Beatriz"]

# Tuple
"Tupla é um tipo que agrupa um conjunto de elementos. A diferença para Lista é que Tuplas são imutáveis, ou seja, após sua definição, Tuplas não podem ser modificadas."
tuple01 = (1,2,3,4,5)
tuple02 = ("Carlos", "Ana", "Beatriz", "Jesus")

# Dictionary (dic)
"Dict é um tipo de dado muito flexível do Python. São utilizados para agrupar elementos através da estrutura de chave e valor, onde a chave é o primeiro elemento seguido por dois pontos e pelo valor. Dicionários possibilitam um tipo de manipulação muito poderosa, chamada de Dict Comprehensions"
altura = {'Amanda': 1.65, 'Ana': 1.60, 'João': 1.70}
peso = {'Amanda': 60, 'Ana': 58, 'João': 68}

# Tipo Complexo (complex)
"Esse tipo normalmente é usado em cálculos geométricos e científicos. Um tipo complexo contem duas partes: a parte real e a parte imaginária, sendo que a parte imaginária contem um j no sufixo. A função complex(real[, imag]) do Python possibilita a criação de números imaginários passando como argumento: real, que é a parte Real do número complexo e o argumento opcional imag, representando a parte imaginária do número complexo."
a = 5+2j
b = 20+6j

print(type(a))
print(type(b))
print(complex(2, 5))
