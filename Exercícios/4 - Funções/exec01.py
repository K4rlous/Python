# Funções

"Você usa a palavra-chave def para definir uma função. Inclua o nome da função, parâmetros entre parênteses e dois pontos. Dentro, adicione o código que a função executará."
def ola():
    print("Olá, Mundo!")

"Chamando Funções: Para chamar a função, use seu nome seguido de parênteses."
ola()

"Argumentos e Parâmetros: Parâmetros são variáveis listadas na definição da função. Argumentos são os valores passados quando você chama a função."
def ola(nome):
    print(f"Olá, {nome}!")

ola("Carlos")

"Valores Padrão: Você pode definir valores padrão para os parâmetros. Se nenhum argumento for fornecido, o valor padrão será usado."
def bemvindo(nome="Usuário"):
    print(f"Olá, {nome}")

bemvindo()
bemvindo("Carlos")