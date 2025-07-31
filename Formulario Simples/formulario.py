import tkinter as tk
from tkinter import messagebox
import csv
import os

def enviar():
    nome = entry_nome.get()
    email = entry_email.get()
    idade = entry_idade.get()
    sexo = sexo_var.get()

    if not nome or not email or not idade or not sexo:
        messagebox.showwarning("Aviso", "Preencha todos os campos!")
        return

    try:
        idade = int(idade)
    except ValueError:
        messagebox.showerror("Erro", "Idade deve ser um número!")
        return

    pasta_destino = r"C:\Users\Antonio Murilo\PyCharmMiscProject"  
    os.makedirs(pasta_destino, exist_ok=True)
    arquivo_csv = os.path.join(pasta_destino, "dados_formulario.csv")

    escrever_cabecalho = not os.path.exists(arquivo_csv)

    with open(arquivo_csv, mode="a", newline="", encoding="utf-8") as arquivo:
        writer = csv.writer(arquivo)
        if escrever_cabecalho:
            writer.writerow(["Nome", "E-mail", "Idade", "Sexo"])
        writer.writerow([nome, email, idade, sexo])

    messagebox.showinfo("Sucesso", "Dados salvos com sucesso!")
   
    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_idade.delete(0, tk.END)
    sexo_var.set("")


janela = tk.Tk()
janela.title("Formulário Básico")

tk.Label(janela, text="Nome:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_nome = tk.Entry(janela)
entry_nome.grid(row=0, column=1)

tk.Label(janela, text="E-mail:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_email = tk.Entry(janela)
entry_email.grid(row=1, column=1)

tk.Label(janela, text="Idade:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_idade = tk.Entry(janela)
entry_idade.grid(row=2, column=1)

tk.Label(janela, text="Sexo:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
sexo_var = tk.StringVar()
sexo_menu = tk.OptionMenu(janela, sexo_var, "Masculino", "Feminino", "Outro")
sexo_menu.grid(row=3, column=1)

btn_enviar = tk.Button(janela, text="Enviar", command=enviar)
btn_enviar.grid(row=4, columnspan=2, pady=10)

janela.mainloop()