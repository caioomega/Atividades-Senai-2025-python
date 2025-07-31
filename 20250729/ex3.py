#crie um programa que leia o conteudo de nomes.txt e copie para um novo arquivo nomes_copia.txt
nome_do_arquivo = "20250729\\nomes.txt"
nome_copia = "20250729\\nomes_copia.txt"
with open(nome_do_arquivo, "r") as arquivo:
    conteudo = arquivo.read()
with open(nome_copia, "w") as arquivo_copia:
    arquivo_copia.write(conteudo)
