opcao = "editar"
match opcao:
    case "novo":
        print("criar novo arquivo")
    case "abrir":
        print("abrir arquivo existente")
    case "editar":
        print("editar arquivo existente")  
    case _:
        print("opção inválida")