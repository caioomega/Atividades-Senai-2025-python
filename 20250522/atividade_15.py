nome = input("Qual é o seu nome? ")
idade = int(input("Qual é a sua idade? "))
cnh = input("Você possui CNH? (sim/não) ")
carro = input("Você possui carro? (sim/não) ")
if idade >= 18:
    if cnh == "sim":
        if carro == "sim":
            print(nome, "Você pode dirigir")
        else:
            print(nome, "Você precisa comprar um carro")
    else:
        print(nome, "Você precisa tirar a CNH")
else:
    print(nome, "Você é muito jovem para dirigir")