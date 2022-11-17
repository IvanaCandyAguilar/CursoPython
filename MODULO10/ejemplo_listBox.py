import sys
import tkinter
from tkinter import ttk
window = tkinter.Tk()

window.columnconfigure(0, weight=1)
window.columnconfigure(0, weight=3)

lista = ['Linux', 'Windows', 'Mas/OS', 'Ms/DOS','Otra lista','Otra lista2']
listaItems = tkinter.StringVar(value=lista)
listBox = tkinter.Listbox(window, height=30, listvariable=listaItems)
listBox.grid(column=0, row=0, sticky=tkinter.W)

window.mainloop()
sys.exit(0)

