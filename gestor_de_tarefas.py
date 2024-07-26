import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0)
    else:
        messagebox.showwarning("Aviso", "Digite uma tarefa.")

def remove_task():
    try:
        index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(index)
    except IndexError:
        messagebox.showwarning("Aviso", "Selecione uma tarefa para remover.")

def mark_done():
    try:
        index = listbox_tasks.curselection()[0]
        task = listbox_tasks.get(index)
        listbox_tasks.delete(index)
        listbox_tasks.insert(tk.END, task + " - Concluída")
    except IndexError:
        messagebox.showwarning("Aviso", "Selecione uma tarefa para marcar como concluída.")

root = tk.Tk()
root.title("Gerenciador de Tarefas")

frame_tasks = tk.Frame(root)
frame_tasks.pack(pady=10)

listbox_tasks = tk.Listbox(frame_tasks, width=50, height=10)
listbox_tasks.pack(side=tk.LEFT)

scrollbar = tk.Scrollbar(frame_tasks)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox_tasks.yview)

entry_task = tk.Entry(root, width=50)
entry_task.pack(pady=10)

button_add = tk.Button(root, text="Adicionar Tarefa", command=add_task)
button_add.pack(pady=5)

button_remove = tk.Button(root, text="Remover Tarefa", command=remove_task)
button_remove.pack(pady=5)

button_done = tk.Button(root, text="Marcar Como Concluída", command=mark_done)
button_done.pack(pady=5)

root.mainloop()
