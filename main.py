import tkinter as tk
from tkinter import ttk, messagebox
from models import Estudiante
import csv_serializer
import helpers

estudiantes = []

def registrar():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    nota1 = entry_n1.get()
    nota2 = entry_n2.get()
    nota3 = entry_n3.get()
    genero = genero_var.get()
    actividades = ";".join([act for act, var in actividades_vars.items() if var.get()])
    email = entry_email.get()

    if not helpers.validar_email(email):
        messagebox.showerror("Error", "Email inválido")
        return

    e = Estudiante(nombre, edad, nota1, nota2, nota3, genero, actividades, email)
    estudiantes.append(e)
    tree.insert("", "end", values=(e.nombre, e.promedio, e.estado))
    limpiar_campos()

def limpiar_campos():
    entry_nombre.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_n1.delete(0, tk.END)
    entry_n2.delete(0, tk.END)
    entry_n3.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    genero_var.set("")
    for var in actividades_vars.values():
        var.set(False)

root = tk.Tk()
root.title("Gestor de Estudiantes")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# Pestaña Registro
frame_registro = ttk.Frame(notebook)
notebook.add(frame_registro, text="Registro")

tk.Label(frame_registro, text="Nombre").grid(row=0, column=0)
entry_nombre = tk.Entry(frame_registro); entry_nombre.grid(row=0, column=1)

tk.Label(frame_registro, text="Edad").grid(row=1, column=0)
entry_edad = tk.Entry(frame_registro); entry_edad.grid(row=1, column=1)

tk.Label(frame_registro, text="Nota 1").grid(row=2, column=0)
entry_n1 = tk.Entry(frame_registro); entry_n1.grid(row=2, column=1)

tk.Label(frame_registro, text="Nota 2").grid(row=3, column=0)
entry_n2 = tk.Entry(frame_registro); entry_n2.grid(row=3, column=1)

tk.Label(frame_registro, text="Nota 3").grid(row=4, column=0)
entry_n3 = tk.Entry(frame_registro); entry_n3.grid(row=4, column=1)

tk.Label(frame_registro, text="Email").grid(row=5, column=0)
entry_email = tk.Entry(frame_registro); entry_email.grid(row=5, column=1)

tk.Label(frame_registro, text="Género").grid(row=6, column=0)
genero_var = tk.StringVar()
tk.Radiobutton(frame_registro, text="Masculino", variable=genero_var, value="Masculino").grid(row=6, column=1)
tk.Radiobutton(frame_registro, text="Femenino", variable=genero_var, value="Femenino").grid(row=6, column=2)

tk.Label(frame_registro, text="Actividades").grid(row=7, column=0)
actividades_vars = {a: tk.BooleanVar() for a in ["Deportes","Música","Arte"]}
col = 1
for act, var in actividades_vars.items():
    tk.Checkbutton(frame_registro, text=act, variable=var).grid(row=7, column=col)
    col += 1

tk.Button(frame_registro, text="Registrar", command=registrar).grid(row=8, column=1)

# Pestaña Visualización
frame_visual = ttk.Frame(notebook)
notebook.add(frame_visual, text="Visualización")

tree = ttk.Treeview(frame_visual, columns=("Nombre","Promedio","Estado"), show="headings")
tree.heading("Nombre", text="Nombre")
tree.heading("Promedio", text="Promedio")
tree.heading("Estado", text="Estado")
tree.pack(fill="both", expand=True)

root.mainloop()
