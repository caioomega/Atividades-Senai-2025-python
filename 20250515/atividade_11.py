
#calculando o IMC de uma pessoa
peso = float(input("Digite o peso em KG: "))
altura = float(input("Digite a altura em metros: "))
imc = peso / altura ** 2
print(f"O IMC é {imc:.2f}")
#na linha 1 e 2 o input server para ler o peso e a altura
#nas linhas 1 e 2 o float signiifica que o valor lido é um numero rea
#na linha 3 o resultado do IMC é calculado
#na linha 4 o resultado é formatado com duas casas decimais
#,2f serve para formatar o resultado com duas casas decimaisl
#na linha 6 o print(f) serve para imprimir o resultado formatado, significar f é uma string 
#que pode conter expressões de formatação
