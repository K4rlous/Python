# Biblioteca Pandas

"Ela é essencial para manipulação e análise de dados em Python. Ela é especialmente popular em data science e machine learning devido à sua capacidade de lidar com grandes conjuntos de dados de maneira eficiente e intuitiva"

# Os outputs de cada operação foram "individualizados"

import pandas as pd

# Estruturas de Dados Principais:

"Series: Uma estrutura unidimensional semelhante a um array."

"DataFrame: Uma estrutura bidimensional (tabela) com rótulos para linhas e colunas."

# Criando uma Series
s = pd.Series([1, 2, 3, 4, 5])
print(s)

# Criando um DataFrame
data = {'Nome': ['Alice', 'Bob', 'Charlie'], 'Idade': [25, 30, 35]}
df = pd.DataFrame(data)
print(df)

# Leitura e Escrita de Dados:

"Leitura de arquivos CSV: pd.read_csv()"
"Escrita em arquivos CSV: df.to_csv()"

# Lendo um arquivo CSV
df = pd.read_csv('dados.csv')

# Escrevendo um DataFrame em um arquivo CSV
df.to_csv('saida.csv', index=False)


# Manipulação de Dados:

"Seleção de Colunas: df['coluna']"
"Filtragem de Dados: df[df['coluna'] > valor]"
"Adição de Colunas: df['nova_coluna'] = valores"
"Remoção de Colunas: df.drop('coluna', axis=1, inplace=True)"

# Filtrando dados
filtrado = df[df['Idade'] > 30]

# Adicionando uma nova coluna
df['Idade_Dobro'] = df['Idade'] * 2


# Agrupamento e Agregação:

"Agrupamento: df.groupby('coluna')"
"Agregação: df.groupby('coluna').agg(funcao)"

# Agrupando por coluna e calculando média
media_idade = df.groupby('Nome')['Idade'].mean()
print(media_idade)


# Operações de Mesclagem:

"Mesclagem (Merge): pd.merge(df1, df2, on='coluna')"

# Mesclando dois DataFrames
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Nome': ['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'ID': [1, 2, 3], 'Idade': [25, 30, 35]})
df_mesclado = pd.merge(df1, df2, on='ID')
print(df_mesclado)
