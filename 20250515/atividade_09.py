#criando um programa que leia um numero inteiro e imorima seu sucessor e antecessor
numero = int(input("Digite um numero inteiro: "))
sucessor = numero + 1
antecessor = numero - 1
print("O antecessor de {} é {} e o sucessor é {}".format(numero,antecessor, sucessor))