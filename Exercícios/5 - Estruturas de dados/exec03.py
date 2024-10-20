# Conjuntos (sets)

"São usados para armazenar coleções de itens únicos e são particularmente úteis para eliminar duplicatas. Eles também são excelentes para operações matemáticas como união, interseção e diferença."

conjunto = {1,2,3,4,5}

# Os outputs de cada operação foram "individualizados"

# Adição
"Usando add(): Adiciona um item ao set."
conjunto.add(6)
print(conjunto) # Saida: {1,2,3,4,5,6} 

"Usando update(): Adiciona múltiplos itens (de outro set, lista, etc.) ao set."
conjunto.update([6,7,8])
print(conjunto) # Saida: {1,2,3,4,5,6,7,8}


# Remoção
"Usando remove(): Remove um item específico. Se o item não existe, gera um erro."
conjunto.remove(2)
print(conjunto) # Saida: {1,3,4,5}

"Usando discard(): Remove um item específico. Se o item não existe, gera um erro"
conjunto.discard(2)
print(conjunto) # Saida: {1,3,4,5}

"Usando pop(): Remove e retorna um item aleatório do set. Como sets são desordenados, não há garantia de qual item será removido."
item = conjunto.pop()
print(conjunto) # Saida possivel: {2,3,4,5}
print(item) # Saida possível: 1

"Usando clear(): Remove todos os itens do set."
conjunto.clear
print(conjunto) # Saida: set()


# Iteração
"Usando for loop:"
for item in conjunto:
    print(item)
    # Saida: 1,2,3,4,5 (Outra ordem possível)