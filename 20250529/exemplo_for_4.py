#somando numeros de intervalo informado limitando o maior numero
inicio = int(input("Digite o número inicial: "))
fim = int(input("Digite o número final: "))
salto = int(input("Digite o salto: "))
texto = 'calculo: '
soma = 0 
for numero in range (inicio , fim , salto):
    soma = soma +numero
    texto = texto + str(numero)
    if numero > 50:
        texto = texto + "\nPassou de 50"
        break
    if numero != fim-1:
        texto = texto + " + "
print(f"{texto}")
print(f"Soma: {soma}")