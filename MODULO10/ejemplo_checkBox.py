import sys
import tkinter
from tkinter import ttk

def mifuncion():
    print('clicado')
window = tkinter.Tk()

window.columnconfigure(0, weight=1)
window.columnconfigure(0, weight=3)


selected = tkinter.StringVar()
checkBox = tkinter.Checkbutton(window, text='Acepto las condiciones', variable='seleccionado', command= mifuncion)
checkBox.grid(column=0, row=0)

window.mainloop()
sys.exit(0)
