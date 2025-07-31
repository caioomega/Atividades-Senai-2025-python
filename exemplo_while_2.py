notas = 0
qntInfo = 0
while True:
    nota = float(input("Digite uma nota (ou -1 para sair): "))
    if nota == -1:
        break
    notas = notas + nota
    qntInfo = qntInfo + 1
if qntInfo > 0:
    media = notas/ qntInfo
    print(f"qintidade de notas: {qntInfo}")
    print(f"Média das notas: {media:.2f}")
else:
    print("Nenhuma nota informada.")