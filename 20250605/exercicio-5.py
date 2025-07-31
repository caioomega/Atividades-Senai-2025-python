idade_media_homens = 0
idade_media_mulheres = 0
idade_media_grupo = 0
idade_homens = 0
idade_mulheres = 0
cont_homens = 0
cont_mulheres = 0
for i in range(5):
    idade = int(input("digite a idade: "))
    sexo = input("digite o sexo (M/F): ")
    if sexo.upper() == "M":
        idade_homens += idade
        cont_homens += 1
    elif sexo.upper() == "F":
        idade_mulheres += idade
        cont_mulheres += 1
        if i == 4:
            idade_media_mulheres = idade_mulheres / cont_mulheres
            idade_media_homens = idade_homens / cont_homens
            idade_media_grupo = (idade_homens + idade_mulheres) / (cont_homens)
            print(f"idade media das mulheres: {idade_media_mulheres:.2f}")
            print(f"idade media dos homens: {idade_media_homens:.2f}")
            print(f"idade media do grupo: {idade_media_grupo/5:.2f}")
        else:
            continue
            