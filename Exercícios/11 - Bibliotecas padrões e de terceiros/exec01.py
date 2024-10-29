# Biblioteca math

"A biblioteca math em Python é uma biblioteca padrão que fornece funções matemáticas úteis, como trigonometria, logaritmos, arredondamentos e mais. É ótima para quando você precisa realizar operações matemáticas avançadas sem reinventar a roda. Aqui estão alguns dos seus destaques:"

"Funções Trigonométricas:"

# math.sin(x): Retorna o seno de x.
# math.cos(x): Retorna o cosseno de x.
# math.tan(x): Retorna a tangente de x.

import math

angulo = math.pi / 4  # 45 graus
print(math.sin(angulo))  # Saída: 0.7071067811865476
print(math.cos(angulo))  # Saída: 0.7071067811865476

"Funções Logarítmicas:"

# math.log(x, base): Retorna o logaritmo de x na base fornecida.
# math.log10(x): Retorna o logaritmo de x na base 10.
# math.log2(x): Retorna o logaritmo de x na base 2.

print(math.log(100, 10))  # Saída: 2.0
print(math.log10(15)) # Saída: 1.1760912590556813
print(math.log2(8))       # Saída: 3.0

"Arredondamento e Outros:"

# math.ceil(x): Arredonda x para cima.
# math.floor(x): Arredonda x para baixo.
# math.sqrt(x): Retorna a raiz quadrada de x.

numero = 8.7
print(math.ceil(numero))   # Saída: 9
print(math.floor(numero))  # Saída: 8
print(math.sqrt(16))       # Saída: 4.0

"Constantes:"

# math.pi: O valor de π (pi).
# math.e: O valor de e (base dos logaritmos naturais).

print(math.pi)  # Saída: 3.141592653589793
print(math.e)   # Saída: 2.718281828459045
