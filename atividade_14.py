#classificar notas
nota = float(input("Digite a nota do aluno: "))
if nota >= 10:
  print("Exelente")
elif nota >= 8:
    print("Bom")
elif nota >= 6:
    print("Satisfatório")
elif nota >= 4:
    print("Ruim")
else:
    print("Pessimo")