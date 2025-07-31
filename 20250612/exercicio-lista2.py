palavras = []
while True:
    palavra = input("Digite uma palavra (0 para sair): ")
    if palavra == "0":
        break
    else:
        palavras.append(palavra)
        palavra = input("Digite a palavra que deseja contar: ")
        if palavra in palavras:
            print(f"A palavra '{palavra}' aparece {palavras.count(palavra)} vezes.")
        else:
            print(f"A palavra '{palavra}' não foi encontrada.")
            break