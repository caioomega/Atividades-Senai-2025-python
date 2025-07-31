#criando um programa para entrar com base a altura de um retangulo e imprimir respectivamente o perimetro e a area correspondete 
base = float(input("Digite a base do retangulo: "))
altura = float(input("Digite a altura do retangulo: "))
perimetro = 2 * (base + altura)
area = base * altura
print(f"o perimetro do retangulo é {perimetro} e a area é {area}")
