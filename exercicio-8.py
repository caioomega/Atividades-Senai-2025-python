#crie um programa utilizando a estrutura for que leia 7 valores inteiros e encontre e mostre o maior valor e o menor, e mostre a media dos numeros lidos
num = 0
soma = 0
for i in range(7):
    num = int(input("Digite um valor: "))
    soma += num
    if i == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
            if num < menor:
                menor = num
print("O maior valor foi: ", maior)
print("O menor valor foi: ", menor)
media = soma / 7
print("A media dos valores foi: ", media)