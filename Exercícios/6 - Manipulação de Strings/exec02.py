# Formatação com f-string ou format()

nome = "Fulano"
idade = 30

"F-strings (a partir do Python 3.6): F-strings permitem a inclusão de expressões dentro das chaves {} diretamente na string."
print(f"Meu nome é {nome} e tenho {idade} anos!")
# Saida: Meu nome é Fulano, e tenho 30 anos!

"format(): O método format() usa placeholders {} que são substituídos pelos valores correspondentes."
mensagem = "Tenho {} anos e me chamo {}!".format(idade, nome)
print(mensagem)
# Saida: Tenho 30 anos, e me chamo Fulano!

"Com índices (no método format()):"
mensagem2 = "Me chamo {0} e essa é a minha idade: {1}. Esse é meu número preferido {1}!".format(nome, idade)
print(mensagem2)
# Saida: Me chamo Fulano e essa é a minha idade: 30. Esse é meu número preferido 30!