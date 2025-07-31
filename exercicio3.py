#criar um programa que peça o nome de 3 alubos e suas respectivas notas, armazene em um dicionário onde a chave é o nome do aluno e o valor é a nota. No final, mostre todos oa alunos com suas notas e media da turma
alunos = {}
for i in range(3):
    nome = input("Digite o nome do aluno: ").strip().title()
    nota = float(input(f"Digite a nota do aluno {nome}: "))
    alunos[nome] = nota
print("\n**" * 30)
print("Alunos e suas notas:")
for aluno, nota in alunos.items():
    print(f"{aluno} - Nota: {nota:.2f}")
media = sum(alunos.values()) / len(alunos)
print(f"\nMédia da turma: {media:.2f}")