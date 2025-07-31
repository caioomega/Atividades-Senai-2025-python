nome_do_arquivo = "20250729\\exemplo4.txt"
with open(nome_do_arquivo, "w") as arquivo:
    arquivo.write("peimeiro\n")
    arquivo.write("segundo\n")
    arquivo.write("terceiro\n")
    
with open(nome_do_arquivo, "r") as arquivo:
    linha = arquivo.readline()
    print(f"1: {linha}")
    
    linha = arquivo.readline(5)
    print(f"2: {linha}")
    
    linha = arquivo.readline(10)
    print(f"3: {linha}")

    linha = arquivo.readline(10)
    print(f"4: {linha}")