# Listas

"Servem para armazenar uma coleção ordenada de itens, que podem ser de tipos diferentes."

lista = [1,2,3,4,5]

# Os outputs de cada operação foram "individualizados"

# Adição
"Usando append(): Adiciona um item ao final da lista."
lista.append(6)
print(lista) # Saida: [1,2,3,4,5,6]

"Usando insert(): Insere um item em uma posição específica."
lista.insert(1, 7) # Saida: [1,7,2,3,4,5] uma vez que inserimos o 7 na posição 1, lembre-se que as posições começam em 0!

"Usando extend(): Adiciona múltiplos itens de outra lista."
lista.extend([6,7,8]) # Saida: [1,2,3,4,5,6,7,8]


# Remoção
"Usando remove(): Remove o primeiro item que corresponde ao valor especificado."
lista.remove(2) # Saida: [1,3,4,5]

"Usando pop(): Remove o item na posição especificada e retorna o valor."
item = lista.pop(1)
print(lista) # Saida: [1,3,4,5]
print(item) # Saida: 2

"Usando clear(): Remove todos os itens da lista."
lista.clear()
print(lista) # Saida: []


# Iteração
"Usando for loop:"
for item in lista:
    print(item) # Saida: 1,2,3,4,5

"Usando while loop:"
i = 0
while i < len(lista): # Enquanto i for menor que o comprimento total da lista...
    print(lista[i]) # Imprima a posição i na lista
    i+=1  # Acrescente 1 em i
    # Saida: 1,2,3,4,5

"Usando List Comprehension:"
[print(item) for item in lista]
# Saida: 1,2,3,4,5