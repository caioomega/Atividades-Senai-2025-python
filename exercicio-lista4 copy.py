import random
nomes = []
while True:
    nome = input("Digite o nome do aluno (ou 'sair' para sair): ")
    if nome.lower() == 'sair':
        break
    nomes.append(nome)
    sorteados = []
    while len(sorteados):
        sorteio = random.choice(nomes)
        if sorteio not in sorteados:
            sorteados.append(sorteio)
            print(sorteados)
            nomes.remove(sorteio)
            print(nomes)
            print(sorteados)
            input("Pressione enter para continuar...")
            print("Sorteio finalizado!") 
            break
        