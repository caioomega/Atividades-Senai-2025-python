#programa que permita registrar a presenca dos alunos em um arquivo, consultar a lista de presença e sair do programa, com uma função pra registrar presença uma pra ver a lista de presença e sair, use o datetime para exibir a data e importe o OS para limpar o terminal
from datetime import datetime
import os
#função para registrar presença
def registrar_presenca():
    pasta = "20250729\\presenca.txt"
    while True:
        nome = input('Digite o nome do aluno ou "sair" para sair: ')
        if nome.lower() == "sair":
            break
        else:
            data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(pasta, "a") as arquivo:
                arquivo.write(f"{nome} {data}\n")
            print(f"Presença de {nome} registrada em {data}")
#função para consultar a lista de presença
def consultar_presenca():
    pasta = "20250729\\presenca.txt"
    if os.path.exists(pasta):
        with open(pasta, "r") as arquivo:
            conteudo = arquivo.readlines()
            if conteudo:
                print("Lista de Presença:")
                for linha in conteudo:
                    print(linha.strip())
            else:
                print("Nenhuma presença registrada.")
    else:
        print("Arquivo de presença não encontrado.")
    print("Nomes arquivados")
# Função para limpar o terminal
def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
# Programa principal
def main():
    while True:
        limpar_terminal()
        print("Menu:")
        print("1. Registrar Presença")
        print("2. Consultar Lista de Presença")
        print("3. Sair")
        escolha = input("Escolha uma opção (1/2/3): ")
        if escolha == "1":
            registrar_presenca()
        elif escolha == "2":
            consultar_presenca()
        elif escolha == "3":
            break
        print("Programa encerrado.")
    else:
        print("Opção inválida. Tente novamente.")
        input("Pressione Enter para continuar...")