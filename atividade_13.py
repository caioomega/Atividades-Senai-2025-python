nome = input("Qual é o seu nome? ")
idade = int(input(f"Olá {nome}, por favor digite a sua idade? "))
if idade > 70:
    print(nome, "Você tem direito ao transporte gratuito")
else:
    print(nome, "Você não tem direito ao transporte gratuito")