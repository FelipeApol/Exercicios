import tkinter as tk

janela = tk.Tk()
janela.configure(bg="lightblue")
janela.title("Minha Primeira Janela")
janela.geometry("400x300")
label = tk.Label(janela, text="Bem-vindo à minha primeira janela!", bg="lightblue", font=("Arial", 14))
label.grid(row=0, column=0, padx=50, pady=30)
button = tk.Button(janela, text="Clique aqui", command=lambda: label2.config(text="Você clicou no botão!"), bg="lightblue", font=("Arial", 12))
button.grid(row=1, column=0, padx=50, pady=50)
label2 = tk.Label(janela, text="", bg="lightblue", font=("Arial", 12))
label2.grid(row=2, column=0, padx=50, pady=10)
janela.mainloop()