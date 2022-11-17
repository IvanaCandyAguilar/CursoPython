import tkinter
from tkinter import ttk
window = tkinter.Tk()

label1 = tkinter.Label(window, text='Posicionamiento absoluto', bg='blue', fg='white')
label1.place(x=40, y=50)

label2 = tkinter.Label(window, text='Otro Posicionamiento absoluto', bg='yellow', fg='black')
label2.place(relx=0.50, rely=0.50, relwidth=0.5, anchor='ne') #siempre a la mitad de la pantalla
#label2.place(x=25, y=30)

window.mainloop()

