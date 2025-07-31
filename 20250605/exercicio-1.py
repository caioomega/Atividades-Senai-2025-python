#criando um programa que verifica a letra digitada pelo usuario é vogal, consoante ou simbolo
letra = input("Digite uma letra: ")
letra = letra.lower()
if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o'or letra == 'u':
    print("A letra digitada é uma vogal.")
else:
    print("a letra é consoante ou é um simbolo!")