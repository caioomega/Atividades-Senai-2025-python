#crie um programa que leia um nome de usuario e sua senha e nao aceite a senha igual o nome de usuario,  mostrando uma mensagem de erro e voltando a pedir as informações ate que estejam certas
nome = input("digite o nome de usuario: ")
senha = input("digite a senha: ")
while senha == nome:
    print("erro, a senha não pode ser igual ao nome de usuario")
    senha = input("digite a senha: ")
    print("senha e nome de usuario criados com sucesso")