# Biblioteca os ! Estudar 

"A biblioteca os permite que você manipule arquivos, diretórios, processos e variáveis de ambiente de forma fácil e eficiente."

"Navegação e Manipulação de Diretórios:"

# os.getcwd(): Retorna o diretório de trabalho atual.
# os.chdir(path): Muda o diretório de trabalho para o especificado.
# os.listdir(path): Lista todos os arquivos e diretórios no caminho especificado.

import os

# Diretório atual
print("Diretório atual:", os.getcwd())

# Mudando o diretório
os.chdir('/tmp')
print("Novo diretório atual:", os.getcwd())

# Listando arquivos e diretórios
print("Conteúdo do diretório:", os.listdir('.'))


"Manipulação de Arquivos:"

# os.rename(src, dst): Renomeia um arquivo ou diretório.
# os.remove(path): Remove um arquivo.
# os.rmdir(path): Remove um diretório vazio.
# os.makedirs(path): Cria diretórios, incluindo diretórios intermediários.

# Renomeando um arquivo
os.rename('arquivo_antigo.txt', 'arquivo_novo.txt')

# Removendo um arquivo
os.remove('arquivo_novo.txt')

# Criando diretórios
os.makedirs('novo/diretorio/estruturado')
  

"Variáveis de Ambiente:"

# os.environ: Um dicionário contendo todas as variáveis de ambiente.
# os.getenv(key): Obtém o valor de uma variável de ambiente.
# os.putenv(key, value): Define o valor de uma variável de ambiente.

# Obtendo uma variável de ambiente
path = os.getenv('PATH')
print("PATH:", path)

# Definindo uma variável de ambiente
os.putenv('MINHA_VARIAVEL', '1234')


"Informações do Sistema:"

# os.name: Nome do sistema operacional (por exemplo, 'posix', 'nt').
# os.uname(): Informações sobre o SO (disponível em Unix).

# os.system(command): Executa um comando no shell do sistema.

# Nome do SO
print("Nome do SO:", os.name)

# Executando um comando no shell
os.system('echo Hello, World!')


"Caminhos de Arquivos:"

# os.path.join(path, *paths): Junta componentes do caminho em um único caminho.
# os.path.exists(path): Verifica se um caminho existe.
# os.path.isfile(path): Verifica se um caminho é um arquivo.
# os.path.isdir(path): Verifica se um caminho é um diretório.

import os

# Juntando caminhos
caminho = os.path.join('diretorio', 'subdiretorio', 'arquivo.txt')
print("Caminho completo:", caminho)

# Verificando a existência de caminhos
print("Arquivo existe?", os.path.exists(caminho))
