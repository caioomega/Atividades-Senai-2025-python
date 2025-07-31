numeros = []
repetidos = []
unicos = []
while True:
    num = int(input('Digite um número (0 para sair): '))
    if num == 0:
        break
    elif num in numeros:
        repetidos.append(num)
    else:
        numeros.append(num)
        unicos = sorted(set(numeros))
        repetidos = sorted([x for x in numeros if numeros.count(x) > 1])
        print(f'Lista de números: {sorted(numeros)}')
        print(f'Lista de números sem repetição: {unicos}')
        print(f'Lista de números repetidos: {repetidos}')