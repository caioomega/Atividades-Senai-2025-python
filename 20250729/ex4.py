pasta = "20250729\\notas.txt"
i=0
while True:
    nome=str(input('Digite o nome ou "sair" para sair: '))
    if nome.lower() == "sair":
        break
    else:
        nota=str(input("digite a nota final do aluno: "))
        with open (pasta, "a") as arquivo:
            arquivo.write(f"{nome} {nota}\n")
            i+=1
print("nomes arquivados")