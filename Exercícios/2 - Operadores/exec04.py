# Operadores Lógicos

n1, n2 = 5, 10

# And  Retorna True se ambas as afirmações forem verdadeiras
if n1 > 3 and n2 < 12:
    print("Ambas condições são verdadeiras!")

# Or   Retorna True se uma das afirmações for verdadeira
if n1 > 4 or n2 > 15:
    print("Uma ou ambas condições são verdadeiras!")

# Not  Retorna Falso se o resultado for verdadeiro
if not (n1 < 10 and n2 < 100):
    print("Inverte o resultado da condição entre os parênteses")