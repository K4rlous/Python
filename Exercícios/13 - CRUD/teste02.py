import mysql.connector
import time

def connect_to_database():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='@',
        database='testepython',
    )

def close_connection(conexao, cursor):
    cursor.close()
    conexao.close()

def tempo():
    time.sleep(1.5)

def main():
    try:
        while True:
            print('#################################')
            op = input('Olá! Escolha a operação que deseja realizar | 1: Criar | 2: Ler | 3: Atualizar | 4: Apagar | 5: Sair | ')
            if op not in ['1', '2', '3', '4', '5']:
                print('Opção inválida, por favor, tente novamente.')
                continue
            if op == '5':
                print('Processo encerrado!')
                break
            operacoes[int(op)]()
    except ValueError:
        print('#################################')
        print('Entrada Inválida, digite um número entre 1 e 4, processo encerrado!')

def criar():
    conexao = connect_to_database()
    cursor = conexao.cursor()
    nome_produto = input('Digite o nome do produto: ')
    try:
        valor = int(input('Digite o valor do produto: '))
        comando = 'INSERT INTO vendas (nome_produto, valor) VALUES (%s, %s)'
        cursor.execute(comando, (nome_produto, valor))
        conexao.commit()
        print('#################################')
        print(f'{nome_produto} adicionado com sucesso, processo encerrado')
    except ValueError:
        print('#################################')
        print('Entrada Inválida, digite um número inteiro, processo encerrado')
    finally:
        close_connection(conexao, cursor)

def ler():
    conexao = connect_to_database()
    cursor = conexao.cursor()
    tempo()
    cursor.execute('SELECT COUNT(*) FROM vendas')
    total_registros = cursor.fetchone()[0]
    print('#################################')
    print(f"Existem {total_registros} registros!")
    cursor.execute('SELECT * FROM vendas')
    registros = cursor.fetchall()
    for registro in registros:
        print(registro)
    print('#################################')
    print('Leitura realizada com sucesso, processo encerrado')
    close_connection(conexao, cursor)

def atualizar():
    ler()
    conexao = connect_to_database()
    cursor = conexao.cursor()
    try:
        op = int(input('O que você deseja atualizar | 1 - Nome do Produto | 2 - Valor | '))
        if op == 1:
            id_vendas = int(input('Digite o ID do produto cujo nome queira mudar: '))
            nome_produto = input('Digite o novo nome do produto: ')
            comando = 'UPDATE vendas SET nome_produto = %s WHERE idVendas = %s'
            cursor.execute(comando, (nome_produto, id_vendas))
        elif op == 2:
            id_vendas = int(input('Digite o ID do produto cujo valor queira mudar: '))
            valor = int(input('Digite o novo valor do produto: '))
            comando = 'UPDATE vendas SET valor = %s WHERE idVendas = %s'
            cursor.execute(comando, (valor, id_vendas))
        else:
            print('Opção inválida, processo encerrado')
            return
        conexao.commit()
        print('#################################')
        print('Atualização realizada com sucesso, operação encerrada!')
    except ValueError:
        print('Entrada Inválida, processo encerrado')
    finally:
        close_connection(conexao, cursor)

def apagar():
    ler()
    conexao = connect_to_database()
    cursor = conexao.cursor()
    try:
        id_vendas = int(input('Digite o ID do produto que deseja apagar: '))
        comando = 'DELETE FROM vendas WHERE idVendas = %s'
        cursor.execute(comando, (id_vendas,))
        conexao.commit()
        print('#################################')
        print(f'Registro com ID {id_vendas} apagado com sucesso, processo encerrado')
    except ValueError:
        print('#################################')
        print('Entrada Inválida, digite um número inteiro, processo encerrado')
    finally:
        close_connection(conexao, cursor)

operacoes = {1: criar, 2: ler, 3: atualizar, 4: apagar}

if __name__ == "__main__":
    main()
