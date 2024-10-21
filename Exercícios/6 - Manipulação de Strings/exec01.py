# Métodos básicos de string len(), upper(), lower(), split(), join().

string = "Batata"
string01 = "Olá, Mundo"
lista =     ["Olá,", "Usuário"]

"len(): Retorna o comprimento (número de caracteres) de uma string."
print(len(string))
# Saida: 6

"upper(): Converte todos os caracteres de uma string para maiúsculas."
print(string.upper())
# Saida: BATATA

"lower(): Converte todos os caracteres de uma string para minúsculas."
print(string.lower())
# Saida: batata

"split(): Divide a string em uma lista de substrings com base em um delimitador."
print(string01.split())
# Saida: ['Olá,', 'Mundo']

"join(): Junta elementos de uma lista em uma única string, usando um delimitador."
print(" ".join(lista))
# Saida: Olá, Usuário