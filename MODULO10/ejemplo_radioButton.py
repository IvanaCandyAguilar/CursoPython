import sys
import tkinter
from tkinter import ttk
window = tkinter.Tk()

window.columnconfigure(0, weight=1)
window.columnconfigure(0, weight=3)


selected = tkinter.StringVar()
r1 = ttk.Radiobutton(window, text='Si', value=1, variable=selected)
r2 = ttk.Radiobutton(window, text='No', value=2, variable=selected)
r3 = ttk.Radiobutton(window, text='Quiza', value=3, variable=selected)

r1.grid(column = 0, row=1, padx=5, pady=5)
r2.grid(column = 0, row=2, padx=5, pady=5)
r3.grid(column = 0, row=3, padx=5, pady=5)

selected2 = tkinter.StringVar()
rs1 = ttk.Radiobutton(window, text='Si2', value=1, variable=selected2)
rs1.grid(column = 1, row=0, padx=5, pady=5)

window.mainloop()
sys.exit(0)
