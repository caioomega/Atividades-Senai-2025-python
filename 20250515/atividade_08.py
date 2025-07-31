#escrevendo um programa que leia dois caracteres(caracter_1 e caracter_2 e imprima-os na tela da seguinte forma "o usuario digitou (caracter_1) e (caracter_2)")
caracter_1 = input("Digite o primeiro caracter: ")
caracter_2 = input("Digite o segundo caracter: ")
print(f"O usuario digitou {caracter_1} E {caracter_2}")
#ou 
print("O usuario digitou {} E {}".format(caracter_1, caracter_2))