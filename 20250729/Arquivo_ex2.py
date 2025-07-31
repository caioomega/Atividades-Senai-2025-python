nome_do_arquivo = "exemplo.txt"

with open(nome_do_arquivo, "a") as arquivo:
    arquivo.write("linha adicionada ao final do arquivo\n")