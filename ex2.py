#utilize o arquivo nomes.txt criado no ex1 abra-o para leitura e mostre cada nome precedido do numero da linha e atualize o arquivo ex 1:caio 2:maria 3:joao
nome_do_arquivo = "20250729\\nomes.txt"
with open(nome_do_arquivo, "r") as arquivo:
    linhas = arquivo.readlines()
for i, linha in enumerate(linhas, start=1):
    print(f"{i}: {linha.strip()}")