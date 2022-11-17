import sys
import tkinter
from tkinter import ttk
window = tkinter.Tk()

def limpiar(event):
    selected.set(None)

window.columnconfigure(0, weight=1)
window.columnconfigure(0, weight=3)

selected = tkinter.StringVar()

r1 = ttk.Radiobutton(window, text='Manzanas', value=1, variable=selected)
r2 = ttk.Radiobutton(window, text='Naranjas', value=2, variable=selected)
r3 = ttk.Radiobutton(window, text='Peras', value=3, variable=selected)

r1.grid(column = 0, row=1, padx=5, pady=5)
r2.grid(column = 0, row=2, padx=5, pady=5)
r3.grid(column = 0, row=3, padx=5, pady=5)

botonLimpiar = tkinter.Button(window, text='Limpiar Seleccion')
botonLimpiar.grid(column=0, row=4, padx=5, pady=5)
botonLimpiar.bind('<Button-1>',limpiar)

window.mainloop()
sys.exit(0)
