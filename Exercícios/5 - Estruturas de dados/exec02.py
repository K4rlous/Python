# Tuplas

"Tuplas em Python são semelhantes a listas, mas com uma diferença crucial: elas são imutáveis, ou seja, uma vez criadas, seus valores não podem ser alterados."

"Tuplas são imutáveis, então a adição e remoção de elementos diretamente não é possível. No entanto, você pode criar novas tuplas baseadas em valores de tuplas existentes. "

tupla = (1,2,3,4,5)

# Os outputs de cada operação foram "individualizados"

# Adição
"Como as tuplas são imutáveis, você pode criar uma nova tupla combinando tuplas existentes."
nova_tupla = tupla + (6,)
print(nova_tupla) # Saida: (1,2,3,4,5,6)


# Remoção
"Para remover um item, você precisa criar uma nova tupla sem o item desejado."
nova_tupla1 = tupla[:2] + tupla[3:]
print(nova_tupla1) # Saida: (1,2,4,5)


# Iteração
"Você pode iterar sobre os elementos de uma tupla usando um loop for, da mesma forma que faria com listas."
for item in tupla:
    print(item)
    # Saida: 1,2,3,4,5