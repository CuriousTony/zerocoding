import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Task list")
root.geometry("400x600")
root.configure(background="wheat1")

text1 = tk.Label(root, text="Введите новую задачу", background="khaki1", font=("Arial", 14, "bold"))
text1.pack(pady=2.5)

task_entry = tk.Entry(root, width=30, bg="snow")
task_entry.pack(pady=2.5)


def add_task():
    try:
        task = task_entry.get().strip().capitalize()
        if not task:
            raise ValueError("Нечего добавлять! Введите что-нибудь.")
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    except ValueError as e:
        """ добавляем фичу - окно с предупреждением """
        messagebox.showerror("Ошибка", str(e))


def task_done():
    try:
        selected_task_indices = task_list.curselection()
        if not selected_task_indices:
            raise IndexError("Выберите задачу для выполнения.")
        for index in selected_task_indices:
            task = task_list.get(index)
            done_task_list.insert(tk.END, task)
            task_list.delete(index)
    except IndexError as e:
        messagebox.showerror("Ошибка", str(e))


def delete_task():
    try:
        selected_task = task_list.curselection()
        if not selected_task:
            raise IndexError("Выберите задачу для удаления.")
        task_list.delete(selected_task)
    except IndexError as e:
        messagebox.showerror("Ошибка", str(e))

add_task_button = tk.Button(root, text="Добавить задачу", command=add_task)
add_task_button.pack(pady=2.5)

task_done_button = tk.Button(root, text="Задача выполнена", command=task_done)
task_done_button.pack(pady=2.5)

delete_task_button = tk.Button(root, text="Удалить задачу", command=delete_task)
delete_task_button.pack(pady=2.5)

text2 = tk.Label(root, text="Список задач:", background="khaki1", font=("Arial", 12, "bold"))
text2.pack(pady=2.5)

task_list = tk.Listbox(root, height=10, width=50, font=("", 12, "italic"))
task_list.pack(pady=2.5)

""" добавляем отдельный список для выполненных задач """
text3 = tk.Label(root, text="Выполненные задачи:", background="khaki1", font=("Arial", 12, "bold"))
text3.pack(pady=2.5)

done_task_list = tk.Listbox(root, height=10, width=50, font=("", 12, "italic"))
done_task_list.pack(pady=2.5)


root.mainloop()