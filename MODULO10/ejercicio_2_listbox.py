import sys
import tkinter
from tkinter import ttk
window = tkinter.Tk()
window.columnconfigure(0, weight=1)
window.columnconfigure(0, weight=3)

label_saludo = tkinter.Label(window,text='Selecciona el navegador que utilizas:',bg='BLUE',fg='WHITE')
label_saludo.grid(column = 0, row=0, padx=5, pady=5)

selected = tkinter.StringVar()

lista = ['Firefox', 'Edge', 'Chrome', 'Opera','Brave','Safari']
listaItems = tkinter.StringVar(value=lista)
listBox = tkinter.Listbox(window, height=20, listvariable=listaItems)
listBox.grid(column=0, row=2, sticky=tkinter.W)

window.mainloop()
sys.exit(0)
