numeros = []
maior = 0
menor = 99999999
soma = 0
mult = 1
while True:
    num = int(input('Digite um número (0 para sair): '))
    soma += num
    if num == 0:
        break
    mult = mult * num
    numeros.append(num)
    if num > maior:
        maior = num
    if num < menor:
            menor = num
print(f"{numeros}")
print(f"{maior}")
print(f"{menor}")
print(f"{soma}")
print(f"{mult}")

        
                