# Uso dos métodos open(), read(), write() e close() / Priorize o uso do gerenciador de contexto descrito no final!

"Abrir Arquivos com open():"

arquivo = open('meuarquivo.txt', 'r')  # Modo de leitura, irá gerar erro pois o arquivo não existe!

"O open() é usado para abrir um arquivo. Ele retorna um objeto de arquivo. Modos comuns de abertura incluem 'r' (leitura), 'w' (escrita), 'a' (acrescentar) e 'b' (modo binário).  Se você usar o modo 'w' (escrita) ou 'a' (acréscimo), o arquivo será criado automaticamente caso não exista. Mas se você abrir o arquivo no modo 'r' (leitura) e ele não existir, um erro será gerado. Portanto, certifique-se de que o arquivo exista antes de tentar lê-lo."

"Ler Arquivos com read():"
# read() lê o conteúdo inteiro do arquivo.
# readline() lê uma linha de cada vez.
# readlines() lê todas as linhas e retorna uma lista.

conteudo = arquivo.read()
print(conteudo)

" Escrever Arquivos com write():"

arquivo = open('meuarquivo.txt', 'w')
arquivo.write('Olá, Mundo!\n')
arquivo.write('Esta é uma nova linha.\n')

"write() escreve uma string no arquivo.Se o arquivo for aberto em modo de escrita ('w'), ele cria um novo arquivo ou sobrescreve um existente. No modo de acrescentar ('a'), ele adiciona conteúdo ao final do arquivo."

"Fechar Arquivos com close():"

arquivo.close()

# Sempre feche o arquivo após terminar de usá-lo para liberar recursos.

"Usando with (Gerenciador de Contexto):"

with open('meuarquivo.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

"O with é uma forma recomendada de abrir arquivos, pois garante que eles serão fechados corretamente. Essa abordagem simplifica a manipulação de arquivos e cuida automaticamente do fechamento."