nome = "caio"
idade = 16

print(f"meu nome é {nome} e minha idade é {idade} anos")
valor = 1234.56789
print(f"o valor é {valor:08.2f}")
#saida: valor é 01234.57

print("Meu nome é {} e eu tenho {} anos".format(nome, idade))
#saida: Meu nome é caio e eu tenho 16 anos

variavel = input("Digite algo: ")
# outro exemplo de input
nome = input("Qual é o seu nome? ")
print("Olá, {}!".format(nome))
#saida: Qual é o seu nome
idade = int(input("Qual é a sua idade? "))
altura = float(input("Qual é a sua altura? "))