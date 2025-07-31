#crie um programa que solicite ao usuario 3 nomes e grave cada nome em uma nova linaha dentro de um arquivo .txt (nomes.txt)
nome_do_arquivo = "20250729\\nomes.txt"
with open(nome_do_arquivo, "w") as arquivo:
    for i in range(3):
        nome = input(f"Digite o nome {i+1}: ")
        arquivo.write(nome + "\n")
#leia o arquivo e exiba seu conteúdo
with open(nome_do_arquivo, "r") as arquivo:
    conteudo = arquivo.read()
    print("Conteúdo do arquivo nomes.txt:")
    print(conteudo)