import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # pip install pillow

# Funções
def abrir_ganhar_peso():
    messagebox.showinfo("💪 Como Ganhar Peso", "Aqui vão as dicas para ganhar peso de forma saudável!")
    print("Vamos ganhar peso?")

def abrir_perder_peso():
    messagebox.showinfo("🔥 Como Perder Peso", "Aqui vão as estratégias para perder peso com saúde!")

def abrir_vida_jejum():
    messagebox.showinfo("⏳ Vida com Jejum", "Entenda os benefícios e cuidados do jejum intermitente!")

def abrir_doce_veneno():
    messagebox.showinfo("🍭 Doce Veneno", "Saiba como o excesso de açúcar afeta sua saúde.")

# Janela principal
janela = tk.Tk()
janela.title("Projeto Saúde")
janela.geometry("500x400")

# Imagem de fundo
imagem_fundo = Image.open("fundo.jpg")  # coloque sua imagem aqui
imagem_fundo = imagem_fundo.resize((500, 400), Image.LANCZOS)
bg_img = ImageTk.PhotoImage(imagem_fundo)

fundo_label = tk.Label(janela, image=bg_img)
fundo_label.place(x=0, y=0, relwidth=1, relheight=1)

# Container escuro sobre a imagem
frame = tk.Frame(janela, bg="#0d1117", bd=0)
frame.place(relx=0.5, rely=0.5, anchor="center")

# Título
titulo = tk.Label(frame, text="🌿 Projeto Saúde", font=("Helvetica", 20, "bold"), fg="#00bcd4", bg="#0d1117")
titulo.pack(pady=(10, 5))

# SubtítulOS
subtitulo = tk.Label(frame, text="Escolha um tema para explorar:", font=("Helvetica", 12), fg="#a0c4ff", bg="#0d1117")
subtitulo.pack(pady=5)

# Estilo dos botões
estilo_botao = {
    "width": 30,
    "bg": "#1f2937",
    "fg": "#a0c4ff",
    "activebackground": "#2563eb",
    "activeforeground": "#ffffff",
    "font": ("Helvetica", 10, "bold"),
    "relief": tk.RAISED,
    "bd": 2
}

# Botões
tk.Button(frame, text="💪 Como Ganhar Peso", command=abrir_ganhar_peso, **estilo_botao).pack(pady=5)
tk.Button(frame, text="🔥 Como Perder Peso", command=abrir_perder_peso, **estilo_botao).pack(pady=5)
tk.Button(frame, text="⏳ Vida com Jejum", command=abrir_vida_jejum, **estilo_botao).pack(pady=5)
tk.Button(frame, text="🍭 Doce Veneno", command=abrir_doce_veneno, **estilo_botao).pack(pady=5)

# Loop
janela.mainloop()

