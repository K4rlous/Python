resposta = 307638730 / 43948390
nome = input("Qual o seu nome? ")
n1 = int(input(f"Olá, {nome}, Vamos digitar dois números? Se a soma deles for igual ao número que estou pensando, você terá uma surpresa! Qual o seu primeiro número? "))
n2 = int(input(f"Legal, seu primeiro número é {n1}, e agora, qual o seu segundo número? "))
print(f"Seus números escolhidos foram {n1} e {n2}, vamos fazer algumas contas com eles? ")
print(f"A soma dos seus números é: {n1 + n2}")
print(f"A subtração dos seus números é: {n1 - n2}")
print(f"A multiplicação dos seus números é: {n1 * n2}")
print(f"A divisão dos seus números é: {n1 / n2}")
print(f"O resto da divisão dos seus números é: {n1 & n2}")
if n1 + n2 != resposta:
    print("Que pena a soma dos seus números não resulta no número que estou pensando, tente de novo!")
else:
    print(f"Como você adivinhou que eu estava pensando no número {resposta}?")
    print("Como prometido aqui está seu prêmio!")
    print("https://matias.me/nsfw/")
    print("Vai sem medo!")
    

