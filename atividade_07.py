#criando um programa para efetuar a leitura de um numero inteiro e apresentar o resultado do quadrado deste numero


numero = int(input("Digite um numero inteiro: "))
quadrado = numero ** 2
print(f"O quadrado do numero {numero} é {quadrado}") 

# outra forma de fazer
numero = int(input("Digite um numero inteiro: "))
quadrado = numero * numero
print("O quadrado do numero {} é {}".format(numero, quadrado))