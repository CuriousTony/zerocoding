import tkinter as tk


def greetings():
    greet = entry.get().title()
    label.config(text=f'Приветствую, {greet}!')


root = tk.Tk()
root.title('Познакомимся?')
root.geometry("300x100")

label = tk.Label(root, text='Введи свое имя: ')
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text='Ввод', command=greetings)
button.pack()

root.mainloop()