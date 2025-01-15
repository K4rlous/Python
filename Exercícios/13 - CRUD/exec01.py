'Os passos serão enumerados aqui e explicados mais detalhadamente no arquivo README presente na pasta do exercício e os comando serão comentados'

#01
import mysql.connector

#02
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='17122000Ch@',
    database='testepython',
)

#03
cursor = conexao.cursor()

# CREATE
''' <- Remova-os!
nome_produto = "chocolate"
valor = 15
comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
cursor.execute(comando)
conexao.commit()
''' 

# READ
"""
comando = 'SELECT * FROM vendas'
cursor.execute(comando)
resultado = cursor.fetchall()
print(resultado)
"""

# UPDATE
"""
nome_produto = "todynho"
valor = 6
comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit()
"""

# DELETE
"""
nome_produto = "todynho"
comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit()
"""

#04
cursor.close()
conexao.close()