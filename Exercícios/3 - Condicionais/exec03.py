# Break, Continue, Pass

"break: Interrompe um loop prematuramente, saindo do bloco de código."
for i in range(10):
    if i == 5:
        break
    print(i)  # Saída: 0 1 2 3 4

"continue: Pula para a próxima iteração do loop, ignorando o código restante no bloco atual."
for i in range(10):
    if i % 2 == 0:
        continue # Se a condição for true, ela cai aqui, continue joga o processo para baixo!
    print(i)  # Saída: 1 3 5 7 9

"pass: Um placeholder para quando uma declaração é necessária, mas você ainda não quer adicionar código. vulgo não faça nada"
for i in range(10):
    if i < 5:
        pass
    else:
        print(i)  # Saída: 5 6 7 8 9