# Biblioteca Numpy

"Ela fornece suporte para arrays multidimensionais (conhecidos como ndarray) e uma variedade de funções matemáticas para operações rápidas em arrays, que são muito mais eficientes do que listas padrão de Python para esse propósito."

# Instalamos ela usando o gerenciador de pacotes pip com o comando:
# pip install numpy

import numpy as np

"Criação de Arrays: NumPy permite criar arrays de diferentes maneiras:"

# Criando um array a partir de uma lista
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# Criando um array de zeros
arr_zeros = np.zeros((3, 3))
print(arr_zeros)

# Criando um array de uns
arr_ones = np.ones((2, 4))
print(arr_ones)

# Criando um array com valores de um intervalo
arr_range = np.arange(0, 10, 2)
print(arr_range)

# Criando um array de valores aleatórios
arr_random = np.random.rand(3, 3)
print(arr_random)


"Operações Aritméticas: Você pode realizar operações matemáticas elementares diretamente nos arrays:"

arr = np.array([1, 2, 3, 4])
print("Array original:", arr)

# Adição
print("Adição:", arr + 2)

# Subtração
print("Subtração:", arr - 2)

# Multiplicação
print("Multiplicação:", arr * 2)

# Divisão
print("Divisão:", arr / 2)


"Indexação e Fatiamento: Assim como listas em Python, você pode acessar e modificar partes de um array NumPy:"

arr = np.array([1, 2, 3, 4, 5])
print("Array original:", arr)

# Indexação
print("Primeiro elemento:", arr[0])
print("Último elemento:", arr[-1])

# Fatiamento
print("Elementos do índice 1 ao 3:", arr[1:4])


"Funções Matemáticas: NumPy oferece diversas funções matemáticas para operações avançadas:"

arr = np.array([1, 2, 3, 4, 5])
print("Array original:", arr)

# Raiz quadrada
print("Raiz quadrada:", np.sqrt(arr))

# Seno
print("Seno:", np.sin(arr))

# Soma total dos elementos
print("Soma:", np.sum(arr))

# Média
print("Média:", np.mean(arr))

# Desvio padrão
print("Desvio padrão:", np.std(arr))


"Operações com Matrizes: Manipulação de matrizes é simples e eficiente com NumPy"

# Criando matrizes
matriz1 = np.array([[1, 2], [3, 4]])
matriz2 = np.array([[5, 6], [7, 8]])

# Multiplicação de matrizes
produto = np.dot(matriz1, matriz2)
print("Produto das matrizes:\n", produto)

# Transposta de uma matriz
transposta = np.transpose(matriz1)
print("Transposta da matriz:\n", transposta)
