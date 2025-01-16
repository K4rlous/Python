import mysql.connector
import time

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='17122000Ch@',
    database='testepython',
)

cursor = conexao.cursor()

def tempo():
    time.sleep(1.5)

def inicio():
    try:
        tempo()
        print('#################################')
        op = int(input('Olá! Escolha a operação que deseja realizar | 1: Criar | 2: Ler | 3: Atualizar | 4: Apagar | '))
        if op == 1:
            criar()
        elif op == 2:
            ler()
        elif op == 3:
            atualizar()
        elif op == 4: 
            apagar()
        else:
            tempo()
            print('#################################')
            print('Opção inválida, processo encerrado')
    except ValueError:
        print('#################################')
        print('Entrada Inválida, digite um número entre 1 e 4, processo encerrado!')

def criar():
    nome_produto = input('Digite o nome do produto: ')
    try:
        valor = int(input('Digite o valor do produto: '))
    except ValueError:
        print('#################################')
        print('Entrada Inválida, digite um número inteiro, processo encerrado')
    comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
    cursor.execute(comando)
    conexao.commit()
    print('#################################')
    print(f'{nome_produto} adicionado com sucesso, processo encerrado')

def ler():
    tempo()
    comando = 'SELECT count(*) FROM vendas'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    print('#################################')
    print(f"Existem {resultado} Registros!")
    comando = 'SELECT * FROM vendas'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    print('#################################')
    print(resultado)
    print('#################################')
    print('Leitura realizada com sucesso, processo encerrado')

def atualizar():
    ler()
    try:
        op = int(input('O que você deseja atualizar | 1 - Nome do Produto | 2 - Valor | '))
    except ValueError:
        print('Entrada Inválida, processo encerrado')
    if op == 1:
        idVendas = int(input('Digite o ID do produto cujo nome queira mudar: '))
        nome_produto = input('Digite o novo nome do produto: ')
        comando = f'UPDATE vendas SET nome_produto = "{nome_produto}" WHERE idVendas = {idVendas}'
        cursor.execute(comando)
        conexao.commit()
        print('#################################')
        print('Atualização realizada com sucesso, operação encerrada!')
    elif op == 2:
        idVendas = int(input('Digite o ID do produto cujo valor queira mudar: '))
        valor = input('Digite o novo valor do produto: ')
        comando = f'UPDATE vendas SET valor = {valor} WHERE idVendas = {idVendas}'
        cursor.execute(comando)
        conexao.commit()
        print('#################################')
        print('Atualização realizada com sucesso, operação encerrada!')
    else:
        print('Opção inválida, processo encerrado')

def apagar():
    ler()
    try:
        idVendas = int(input('Digite o ID do produto que deseja apagar: '))
    except ValueError:
        print('#################################')
        print('Entrada Inválida, digite um número inteiro, processo encerrado')

    comando = f'DELETE FROM vendas WHERE idVendas = {idVendas}'
    cursor.execute(comando)
    conexao.commit()
    print('#################################')
    print(f'Registro com ID {idVendas} apagado com sucesso, processo encerrado')
    

inicio()
cursor.close()
conexao.close()
