
import tkinter as tk
from tkinter import messagebox

# Janela principal
janela = tk.Tk()
janela.title("MEU APLICATIVO")
janela.geometry("400x300")

# Título
titulo = tk.Label(janela, text="MEU APLICATIVO", font=("\033;45Helvetica", 18, "bold"))
titulo.pack(pady=10)

# Botões de navegação
tk.Button(janela, text="CLIQUE AQUI!",width=50).pack(pady=5)

# Funções para cada tema
def abrir_clique_aqui():
    messagebox.showinfo("Seja bem vindo!")

janela.mainloop()



#"\033[0;33;44m", 