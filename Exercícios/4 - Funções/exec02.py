# Funções Anônimas (Lambdas)

"são funções pequenas e sem nome definidas com a palavra-chave lambda. Elas são usadas para criar funções curtas que são utilizadas apenas uma vez ou que não precisam ser nomeadas."
# Função lambda para adicionar 10 a um número
adc_10 = lambda x: x + 10
print(adc_10(5))  # X equivale ao 5, logoo temos a saída: 15

"As lambdas são frequentemente usadas com funções que aceitam outras funções como argumentos, como map(), filter() e sorted()"
numeros = [1, 2, 3, 4, 5]

# Usando lambda para multiplicar cada número por 2
resultado1 = map(lambda x: x * 2, numeros)
print(list(resultado1))  # Saída: [2, 4, 6, 8, 10]

# Usando lambda para filtrar números ímpares
resultado2 = filter(lambda x: x % 2 != 0, numeros)
print(list(resultado2))  # Saída: [1, 3, 5]