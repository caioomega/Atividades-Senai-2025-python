altura = float(input("Digite a altura do reservatório em cm: "))
largura = float(input("Digite a largura do reservatório em cm: "))
comprimento = float(input("Digite o comprimento do reservatório em cm: "))
consumo = float(input("Digite o consumo médio diário em litros: "))
capacidade = (altura * largura * comprimento) / 1000
autonomia = capacidade / consumo
if capacidade > 0:
    if autonomia > 7:
        classificacao = "consumo reduzido"
    elif autonomia > 2:
        classificacao = "consumo moderado"
    else:
        classificacao = "consumo elevado"
else:
    classificacao = "reservatório vazio ou inválido"
print(f"capacidade total do reservatório: {capacidade:.2f} litros")
print(f"autonomia do reservatório: {autonomia:.2f} dias")
print(f"classificação do consumo: {classificacao}")
    