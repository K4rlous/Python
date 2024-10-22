# 1. Criação e Escrita em Arquivo
with open('dados.txt', 'w') as arquivo:
    arquivo.write("1,John,Doe,25\n")
    arquivo.write("2,Jane,Smith,30\n")
    arquivo.write("3,Bob,Johnson,22\n")
    arquivo.write("4,Alice,Davis,29\n")

# 2. Leitura e Processamento de Arquivo
with open('dados.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

# 3. Manipulação dos Dados com compreensão de listas
dados = [tuple(linha.strip().split(',')) for linha in linhas]

# 4. Filtragem de Dados, baseado na terceira posição (idade) para mostrar aqueles com mais de 25 anos
filtrados = [dado for dado in dados if int(dado[3]) >= 25]

# 5. Resultado Final
with open('resultado.txt', 'w') as arquivo:
    for dado in filtrados:
        linha = f'ID: {dado[0]}, Nome: {dado[1]}, Sobrenome: {dado[2]}, Idade: {dado[3]}\n'
        arquivo.write(linha)


"Esse exemplo de ordenação de dados não foi feito sozinho, foque em aprender mais compreensão de listas!"