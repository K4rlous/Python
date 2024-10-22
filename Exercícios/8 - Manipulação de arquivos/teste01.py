with open('teste01.txt', 'w') as teste:
    teste.write("Olá mundo!\n")
    
with open('teste01.txt', 'a') as teste:
    teste.write("Essa linha foi adicionada posteriomente!\n")

with open('teste01.txt', 'r') as teste:
    conteudo = teste.read()
    print(conteudo)
    
# A estrutura with open já fecha automaticamente o arquivo!