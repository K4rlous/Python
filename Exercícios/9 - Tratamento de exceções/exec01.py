#  Exceções com try, except, else e finally.

"Eles são usados para lidar com erros que podem ocorrer durante a execução do programa, permitindo que você controle o fluxo de execução mesmo quando ocorrem erros."

try:
    # Tentar dividir por zero
    resultado = 10 / 0
except ZeroDivisionError: # Algumas exceções possuem nome 'próprio' bem autoexplicativo, como neste exemplo e no abaixo!
    # Tratar a exceção de divisão por zero
    print("Erro: Não é possível dividir por zero.")
else:
    # Este bloco é executado se nenhuma exceção ocorreu
    print("Divisão realizada com sucesso:", resultado)
finally:
    # Este bloco é sempre executado
    print("Operação de divisão finalizada.")

try:
    # Tentar ler um arquivo que não existe!
    arquivo = open("arquivo.txt", "r")
    conteudo = arquivo.read()
except FileNotFoundError: # Note o nome da exceção!
    print("Erro: Arquivo não encontrado.")
else:
    print("Conteúdo do arquivo:", conteudo)
finally:
    arquivo.close() if 'arquivo' in locals() else None
     #if 'arquivo' in locals(): Verifica se a variável arquivo existe no escopo local (ou seja, se ela foi definida e está acessível).arquivo.close(): Se a variável arquivo existir, o método close() será chamado para fechar o arquivo. else None: Se a variável arquivo não existir, a expressão avalia None e nada acontece. Isso evita um erro caso arquivo não esteja definido.
    print("Arquivo fechado, se foi aberto.")

"se o arquivo não for encontrado, a exceção FileNotFoundError será tratada, e a mensagem 'Erro: Arquivo não encontrado' será exibida. Se não houver exceção, o conteúdo do arquivo será exibido. O bloco finally garante que o arquivo seja fechado se foi aberto"

try:
    numero = 9 / 2
except:
    print('Erro ao efetuar divisão!')
else:
    print('Divisão realizada com sucesso', numero)
finally:
    print('Operação Terminada!')