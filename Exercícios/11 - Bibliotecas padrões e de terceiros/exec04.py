# Biblioteca Tkinter

"Tkinter é a biblioteca padrão do Python para criação de interfaces gráficas (GUI)."

# Componentes Principais do Tkinter:

"Janela Principal: A janela principal é a base de qualquer aplicativo Tkinter. Você cria a janela principal usando a classe Tk."

"Widgets: Widgets são os elementos gráficos que você pode adicionar à janela, como botões, rótulos, caixas de texto, etc. Alguns dos widgets mais comuns incluem:"
"Label: Exibe texto ou imagens."
"Button: Cria um botão que pode executar uma função quando clicado."
"Entry: Caixa de entrada para o usuário digitar texto."
"Frame: Contêiner para organizar outros widgets."
"Canvas: Área para desenhar gráficos."

# Gerenciadores de Layout: Tkinter fornece três gerenciadores de layout para organizar widgets dentro da janela:

"pack(): Organiza widgets de cima para baixo ou da esquerda para a direita."
"grid(): Organiza widgets em uma grade (linha e coluna)."
"place(): Coloca widgets em posições absolutas dentro da janela."

# Exemplo básico

import tkinter as tk

# Criando a janela principal
root = tk.Tk() # cria a janela principal.
root.title("Meu Primeiro Programa Tkinter")

# Criando um rótulo (label)
label = tk.Label(root, text="Olá, Mundo!") # cria um rótulo com o texto "Olá, Mundo!".
label.pack(pady=10)

# Criando um botão
def clique():
    label.config(text="Botão Clicado!")

button = tk.Button(root, text="Clique Aqui", command=clique) # cria um botão que, ao ser clicado, chama a função clique, que muda o texto do rótulo.
button.pack(pady=5)

# Iniciando o loop principal
root.mainloop() # inicia o loop principal da interface gráfica, permitindo que o programa responda a eventos (como cliques de botão).
