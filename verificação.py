import tkinter as tk
from tkinter import messagebox, simpledialog

# Lista de convidados
convidados = []

# Função para verificar login
def verificar_login():
    nome = simpledialog.askstring("Login", "Digite seu nome: ")
    idade = simpledialog.askinteger("Login", "Digite sua idade: ")
    if idade is None or idade < 18:
        messagebox.showerror("Erro", "Você deve ter mais de 18 anos para acessar.")
        return

    nota1 = simpledialog.askfloat("Login", "Digite a primeira nota: ")
    nota2 = simpledialog.askfloat("Login", "Digite a segunda nota: ")
    nota3 = simpledialog.askfloat("Login", "Digite a terceira nota: ")
    media = (nota1 + nota2 + nota3) / 3

    if media < 10:
        messagebox.showerror("Erro", "Sua média deve ser 10 ou superior para acessar.")
        return

    messagebox.showinfo("Sucesso", f"Bem-vindo, {nome}!")
    abrir_menu()

# Função para abrir o menu principal
def abrir_menu():
    menu = tk.Toplevel(root)
    menu.title("Gerenciamento de Convidados para a Festa")
    menu.geometry("400x400")
    menu.configure(bg="#f0f8ff")

    tk.Label(menu, text="Gerenciamento de Convidados", font=("Arial", 16, "bold"), bg="#f0f8ff").pack(pady=10)

    def adicionar_convidado():
        nome = simpledialog.askstring("Adicionar Convidado", "Digite o nome do convidado:")
        if nome:
            convidados.append(nome)
            atualizar_lista()
            messagebox.showinfo("Sucesso", f"{nome} foi adicionado à lista de convidados!")

    def remover_convidado():
        nome = simpledialog.askstring("Remover Convidado", "Digite o nome do convidado a remover:")
        if nome in convidados:
            convidados.remove(nome)
            atualizar_lista()
            messagebox.showinfo("Sucesso", f"{nome} foi removido da lista de convidados!")
        else:
            messagebox.showerror("Erro", "Convidado não encontrado.")

    def editar_convidado():
        nome_antigo = simpledialog.askstring("Editar Convidado", "Digite o nome do convidado a editar:")
        if nome_antigo in convidados:
            nome_novo = simpledialog.askstring("Editar Convidado", "Digite o novo nome do convidado:")
            if nome_novo:
                index = convidados.index(nome_antigo)
                convidados[index] = nome_novo
                atualizar_lista()
                messagebox.showinfo("Sucesso", f"{nome_antigo} foi atualizado para {nome_novo}!")
        else:
            messagebox.showerror("Erro", "Convidado não encontrado.")

    def atualizar_lista():
        lista_convidados.delete(0, tk.END)
        for convidado in convidados:
            lista_convidados.insert(tk.END, convidado)

    # Botões do menu
    tk.Button(menu, text="Adicionar Convidado", command=adicionar_convidado, bg="#add8e6", font=("Arial", 12)).pack(pady=5)
    tk.Button(menu, text="Remover Convidado", command=remover_convidado, bg="#ffcccb", font=("Arial", 12)).pack(pady=5)
    tk.Button(menu, text="Editar Convidado", command=editar_convidado, bg="#90ee90", font=("Arial", 12)).pack(pady=5)

    # Lista de convidados
    tk.Label(menu, text="Lista de Convidados", font=("Arial", 14, "bold"), bg="#f0f8ff").pack(pady=10)
    lista_convidados = tk.Listbox(menu, width=40, height=10, font=("Arial", 12))
    lista_convidados.pack(pady=10)

# Configuração da janela principal
root = tk.Tk()
root.title("Sistema de Login e Gerenciamento de Convidados")
root.geometry("400x300")
root.configure(bg="#f0f8ff")

tk.Label(root, text="Bem-vindo ao Sistema de Gerenciamento de Convidados", font=("Arial", 14, "bold"), bg="#f0f8ff").pack(pady=20)
tk.Button(root, text="Fazer Login", command=verificar_login, width=20, bg="#add8e6", font=("Arial", 12)).pack(pady=20)

# Iniciar o loop da interface gráfica
root.mainloop()
