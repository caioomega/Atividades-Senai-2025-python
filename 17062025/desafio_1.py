
contatos = {}
while True:
    nome = input("(digite fim para sair) Digite seu nome: ")
    if nome.lower() == "fim":
        break
    telefone = input("Telefone: ")
    email = input("E-mail: ")
    contatos[nome] = {
        "telefone": telefone,
        "email": email
    }
for contato in contatos:
    print(f"Nome: {contato} | Telefone: {contatos[contato]['telefone']} | E-mail: {contatos[contato]['email']}")
    