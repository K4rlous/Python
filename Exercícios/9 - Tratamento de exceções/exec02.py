# Exceções Personalizadas

# Definindo uma exceção personalizada chamada MinhaExcecao que herda da classe Exception
class MinhaExcecao(Exception):
    # O método __init__ é o construtor da classe e inicializa os atributos mensagem e codigo
    def __init__(self, mensagem, codigo):
        self.mensagem = mensagem  # Atribui a mensagem de erro ao atributo mensagem
        self.codigo = codigo  # Atribui o código de erro ao atributo codigo
    
    # O método __str__ define a representação em string da exceção
    def __str__(self):
        # Retorna uma string formatada com o código de erro e a mensagem de erro
        return f'Erro {self.codigo}: {self.mensagem}'

# Função que lança a exceção personalizada se a divisão por zero for tentada
def dividir(a, b):
    # Verifica se o divisor é zero
    if b == 0:
        # Lança a exceção personalizada MinhaExcecao com uma mensagem e um código de erro
        raise MinhaExcecao("Divisão por zero não é permitida", 400)
    # Retorna o resultado da divisão se não houver erro
    return a / b

# Bloco try-except para capturar e tratar exceções
try:
    # Chama a função dividir com 10 e 0, o que causará uma exceção
    resultado = dividir(10, 0)
# Captura a exceção personalizada MinhaExcecao
except MinhaExcecao as e:
    # Imprime a representação em string da exceção, definida no método __str__
    print(e)  # Saída: Erro 400: Divisão por zero não é permitida
else:
    # Este bloco é executado se nenhuma exceção ocorreu
    print("Divisão realizada com sucesso:", resultado)
finally:
    # Este bloco é sempre executado, independentemente de uma exceção ocorrer ou não
    print("Operação de divisão finalizada.")

"Esse exemplo de exceções personalizadas não foi feito sozinha, foque em aprender mais o tópico!"