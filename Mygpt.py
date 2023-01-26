import tkinter as tk
from tkinter import ttk
import openai

openai.api_key = "[VOTRE_CLES_API"


def myGPT():
    interact = entry.get()
    response = openai.Completion.create(engine="text-davinci-002",
        prompt=interact,
        max_tokens=2048
    )
    text.config(state=tk.NORMAL)
    text.insert(tk.INSERT, response["choices"][0]["text"]+'\n')
    text.config(state=tk.DISABLED)

root = tk.Tk()
root.title("MyGPT")
root.geometry("800x600")

# Utilisation de la bibliothèque ttk pour améliorer l'apparence de l'interface graphique
style = ttk.Style()
style.configure("TButton", font=("Arial", 12))
style.configure("TLabel", font=("Arial", 14))
style.configure("TEntry", font=("Arial", 14))

label = ttk.Label(root, text="Entrez votre question : ")
label.pack()

entry = ttk.Entry(root)
entry.pack()

button = ttk.Button(root, text="Envoyer", command=myGPT)
button.pack()

text = tk.Text(root,font=("Arial", 14))
text.pack()
text.config(state=tk.DISABLED)

root.mainloop()
