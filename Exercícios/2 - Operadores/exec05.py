# Operadores de Identidade

lista01 = [1, 2, 3]
lista02 = [1, 2, 3]
lista03 = lista01

tupla01 = (1,2,3)
tupla02 = (1,2,3)
tupla03 = (3,4,5)

# Operador is	Retorna True se ambas as variáveis são o mesmo objeto
print(f"São o mesmo objeto? {lista01 is lista03}") # São o mesmo objeto!
print(f"São o mesmo objeto? {lista01 is lista02}") # Não são o mesmo objeto!

# Operador is not	Retorna True se ambas as variáveis não forem o mesmo objeto
print(f"Os objetos são diferentes? {tupla01 is not tupla02}") # São o mesmo objeto
print(f"Os objetos são diferentes? {tupla01 is not tupla03}") # São objetos diferentes

" o operador == verifica os valores testados, enquanto o operador is testa a referência dos valores testados"