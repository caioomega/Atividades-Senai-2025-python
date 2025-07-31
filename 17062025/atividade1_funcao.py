#função soma
def soma(n1,n2):
    soma - n1 + n2
    return soma
# subtração
def subtracao(n1, n2):
    subtracao = n1 - n2
    return subtracao
#codigo principal
print("bem vindo a a calculardora")
num1=int(input("digite o primeiro numero: "))
num2=int(input("digite o segundo numero: "))
op=int(input("digite 1 para soma, 2 para subtração: "))
if op == 1:
    resultado = soma(num1, num2)
    print(f"a soma de {num1} + {num2} é igual a {resultado}")
elif op == 2:
    resultado = subtracao(num1, num2)
    print(f"a subtração de {num1} - {num2} é igual a {resultado}")
else:
    print("opção inválida, tente novamente")
