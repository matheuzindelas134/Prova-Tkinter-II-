import tkinter as tk
from tkinter import messagebox

def verificar_login():
    email = entry_email.get()
    senha = entry_senha.get()

    if len(senha) <= 6:
        messagebox.showerror("Erro", "A senha deve ter mais de 6 dígitos.")
        return

    if "@" not in email:
        messagebox.showerror("Erro", "O e-mail deve conter o caractere '@'.")
        return

    messagebox.showinfo("Sucesso", "Login bem-sucedido!")

root = tk.Tk()
root.title("Tela de Login")
root.geometry("300x200")

label_email = tk.Label(root, text="Digite seu E-mail:")
label_email.pack(pady=5)
entry_email = tk.Entry(root, width=30)
entry_email.pack(pady=5)

label_senha = tk.Label(root, text="Digite sua Senha:")
label_senha.pack(pady=5)
entry_senha = tk.Entry(root, show='*', width=30)
entry_senha.pack(pady=5)

button_login = tk.Button(root, text="Entrar", command=verificar_login)
button_login.pack(pady=20)

root.mainloop()