CRUD EM PYTHON (sem flask ou django)

Para realizar a integração do MySQL com o Python devemos usar um driver que pode ser instalado via pip diretamente pelo seu editor de código, ele irá integrar ambos e será a fonte da biblioteca que iremos utilizar!

python -m pip install mysql-connector-python

Após instalar o driver, vamos importar a biblioteca com:

01- import mysql.connector

Feito isso devemos conectar o banco de dados ao Python, porém para isso o banco
de dados deve já ter sido criado no seu MySQL (usamos o workbench)
Precisaremos saber a senha e o usuário do workbench para acessar o banco de dados e fazer a conexão (para facilitar saiba que o usuário padrão é root e a senha é justamente aquela lá rsrs) apenas um lembrete de que o SCHEMA ou banco de dados já deve ter sido criado no workbench!

Criaremos um banco de dados chamado 'testepython' e algumas tabelas dentro dele, a criação de dados com o crud será relativa a criação de informação, isso é dados para as tabelas (apesar de ser possível criar tabelas com o python também!)
As tabelas são idvendas (int, pk, autoincrement) nome_produto (varchar(45)) e valor (int)

02- Então criaremos a conexão entre o MySQL e o Python atribuindo alguns dados a uma variável que iremos chamar de conexao, os quatro dados atribuidos a essa variável são host, user, password e database:

host = como estamos usando um banco de dados armazenado no proprio computador usaremos 'localhost', se por acaso estivéssemos usando um db armazenado em um link específico, colocariamos o link neste campo, ip, enfim

user = mesmo usuário que usamos para acessar o banco de dados no workbench

password = mesma senha que usamos para acessar o banco de dados no workbench

database = o nome do bd que estamos usando, neste caso é 'testepython'

03- Para realizar a conexão precisaremos de um cursor, ele irá executar os comandos a conexão, no caso chamaremos ele simplesmente de cursor, sua sintaxe será: 'cursor = conexao.cursor()'

04- É importante fechar a conexão e o cursor no final do código! para isso usaremos os comandos baseados no cursor e na variável conexao:

cursor.close()
conexao.close()

Lembre-se que eles devem ficar no final do código, após todas as operações!

Teste com os comandos, em suma não acontecerá nada, a conexão irá acontecer e será encerrada sem nenhum problema!

CRUD

Os comandos do crud são basicamente comandos SQL atribuidos a variáveis em python, ou seja quando chamamos as variáveis executamos esses comandos, é recomendado que esses comandos sejam escritos em aspas simples '' e as coisas dentro dele como strings por exemplo devem usar aspas duplas "" caso seja necessário!
Basicamente ficaria assim:

comando = '' (lembre-se aspas simples)

cursor.execute(comando) usaremos o cursor para executar o comando!

conexao.commit() deve ser usado se criamos, atualizamos, ou apagamos dados ou seja EDIÇÃO

resultado = cursor.fetchall() irá ser usado se quisermos armazenar informações ou seja LEITURA

Todas as operações terão 3 dessas quatro etapas obrigatóriamente!



CREATE

nome_produto = "todynho" - NOME DO PRODUTO A SER INSERIDO

valor = 3 - VALOR DO PRODUTO A SER INSERIDO (CUIDADO COM INT, DEC E ETC)

comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})' - NOTE QUE O CÓDIGO É EM SUMA UM COMANDO SQL COM ALGUMAS DIFERENÇAS USAMOS f PARA PERMITIR O USO DE {}, O GRANDE SEGREDO É AS ASPAS DUPLAS "" USADAS EM "{nome_produto}"

cursor.execute(comando) - AUTOEXPLICATIVO
conexao.commit() - AUTOEXPLICATIVO

Perceba que não precisamos inserir o id do produto, pois ele foi definido com auto incremento, se quisermos inserir mais alguma coisa basta mudar o valor das variáveis!



READ

comando = 'SELECT * FROM vendas' - MAIS UM COMANDO SQL

cursor.execute(comando) - AUTOEXPLICATIVO

resultado = cursor.fetchall() - AUTOEXPLICATIVO

print(resultado) - AUTOEXPLICATIVO

Note que os comandos podem simplesmente ser copiados do workbench e jogados aqui, contanto que o fetchall ou o commit aconteça!



UPDATE

nome_produto = "todynho" - NOME DO PRODUTO A SER ALTERADO

valor = 6 - O VALOR DESIGNADO PARA O PRODUTO

comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"' - PERCEBA QUE É MAIS UM COMANDO SQL USANDO VARIÁVEIS, E NOTE O USO DE "" AO REFERENCIAR A VARIÁVEL 'nome_produto'

cursor.execute(comando) - AUTOEXPLICATIVO

conexao.commit() - AUTOEXPLICATIVO



DELETE

nome_produto = "todynho"
comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit()

Perceba que os comandos são em sua maioria simples e bem autoexplicativos, é possível rodar qualquer comando SQL através do Python, as vezes comandos como delete podem ser limitados pelo gerenciador do db então se atente a isso!