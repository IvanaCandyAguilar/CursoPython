import sys
import tkinter
from tkinter import ttk

window = tkinter.Tk()

def salir(event):
    print('Adios')
    window.quit()

def saludar(event):
    print('Han hecho clic en saludar')

def saludardobleclic(event):
    print('Han hecho doble clic en saludar')


boton = tkinter.Button(window, text='Haz clic')
boton.pack()
boton.bind('<Button-1>',saludar)
boton.bind('<Double-1>',saludardobleclic)

botonSalir = tkinter.Button(window, text='Salir')
botonSalir.pack()
botonSalir.bind('<Button-1>',salir)

window.mainloop()
sys.exit(0)
