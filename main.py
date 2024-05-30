from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import *
root = Tk()
def save():
	name = e.get()
	textension = Text.get(1.0, END)
	file = filedialog.asksaveasfile(title = "Сохранить", defaultextension = '.txt',
	initialfile = f'{name}')
	file.write(textension)
def about():
	showinfo(title = "About", message = 'Заметки | (C) Илья Кривоус | Версия 0.1 ')
menu = Menu(root)
file = Menu(menu, tearoff = 0)
file.add_command(label = "Save", command = save)
file.add_separator()
file.add_command(label = "Exit", command = root.quit)
menu.add_cascade(label = 'File', menu = file)
Help = Menu(menu, tearoff = 0)
Help.add_command(label = "About", command = about)
menu.add_cascade(label = 'Help', menu = Help)
e = Entry(root, bg = 'black', 
fg = 'yellow', 
width = 600)
e.insert(0, 'Названия заметки')
e.pack()
Text = Text(root, bg = "black",
fg = 'yellow',
width = 500,
height = 10000000)
Text.insert(1.0, 'Заметкa')
Text.pack()
root.config(menu = menu)
root.mainloop()
