# Condicionais 

n1, n2 = 10, 100

"If Statement (Se): Verifica se uma condição é verdadeira e executa o bloco de código associado."
if n1 < 50:
    print("A condição é verdadeira!")  # bloco de código a ser executado se a condição for verdadeira

"Elif Statement (Se não, se): Verifica uma nova condição se a condição anterior for falsa."
if n1 > 50:
    print("A condição é verdadeira")  # bloco de código a ser executado se condição1 for verdadeira
elif n2 > 90:
    print("Condição 1 é falsa, mas condição 2 é verdadeira!") # bloco de código a ser executado se condição1 for falsa e condição2 for verdadeira

"Else Statement (Se não): Executa um bloco de código se todas as condições anteriores forem falsas."
if n1 > 20:
    print("A condição é verdadeira") # bloco de código a ser executado se condição1 for verdadeira
elif n2 > 200:
    print("A condição 1 é falsa, mas a condição 2 é verdadeira") # bloco de código a ser executado se condição1 for verdadeira
else:
    print("Nenhuma das condições é verdadeira") # bloco de código a ser executado se todas as condições forem falsas

idade = 20

if idade < 18:
    print("Você é menor de idade.")
elif idade >= 18 and idade < 65:
    print("Você é um adulto.")
else:
    print("Você é um idoso.")