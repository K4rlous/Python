# Dicionários 

"São estruturas de dados que armazenam pares de chave-valor. São ótimos para situações em que você precisa associar um conjunto de valores a chaves únicas e, depois, acessar esses valores de forma eficiente usando as chaves."

"Cada chave em um dicionário deve ser única, você pode adicionar, remover e modificar itens, não Ordenados (antes do Python 3.7): a ordem dos itens não é garantida, acesso aos valores é rápido e eficiente através das chaves."

dicionario = {"Pessoa1": "Carlos", "Pessoa2": "Ana", "Pessoa3": "Beatriz"}

# Os outputs de cada operação foram "individualizados"

# Adição
"Você pode adicionar um novo par chave-valor simplesmente atribuindo um valor a uma chave."
dicionario["Pessoa4"] = "Miguel"
print(dicionario) # Saida: {'Pessoa1': 'Carlos', 'Pessoa2': 'Ana', 'Pessoa3': 'Beatriz', 'Pessoa4': 'Miguel'}


# Remoção
"Usando del: Remove um item do dicionário usando a chave."
del dicionario["Pessoa2"]
# Saida: {"Pessoa1": "Carlos", "Pessoa3": "Beatriz"}

"Usando pop(): Remove um item do dicionário e retorna o valor associado à chave removida."
valor = dicionario.pop("Pessoa1")
print(dicionario) # Saida: "Pessoa2": "Ana", "Pessoa3": "Beatriz"}
print(valor) # Saida: Carlos

"Usando popitem():Remove e retorna o último par chave-valor inserido."
chave, valor = dicionario.popitem()
print(dicionario) # Saida: {"Pessoa1": "Carlos", "Pessoa2": "Ana"}
print(chave, valor) # Saida: Pessoa3 Beatriz


# Iteração
"Iteração em Dicionários: Iterar sobre chaves:"
for Pessoa in dicionario:
    print(Pessoa)
    # Saida: Pessoa1 Pessoa2 Pessoa3

"Iterar sobre valores:"
for nome in dicionario.values():
    print(nome)
    # Saida: Carlos Ana Beatriz

"Iterar sobre itens (pares chave-valor):"
for Pessoa, nome in dicionario.items():
    print(f"Pessoa: {Pessoa}, Nome: {nome}")
    # Saida: "Pessoa: Carlos", "Pessoa: Ana", "Pessoa: Beatriz"
    