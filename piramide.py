#faça uma calculadora
def calculadora():
    print("Calculadora")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    escolha = int(input("Escolha uma opção: "))
    if escolha == 1:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print(f"A soma é: {num1 + num2}")
        