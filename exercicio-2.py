#criando um programa que exiba quantas vogais tem na frase que o usuario digitar
frase = str(input('Digite uma frase: ')).lower()
contagem = 0
for letra in frase:
    if letra in 'aeiou':
        contagem += 1
print(f'A frase contém {contagem} vogais.')