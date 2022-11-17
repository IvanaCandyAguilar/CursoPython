import random
import tkinter
from tkinter import ttk
window = tkinter.Tk()

colors=['blue', 'orange', 'yellow', 'red','purple','green','black']

for x in range(0,50):
    color  = random.randint(0,len(colors)-1)
    color2 = random.randint(0,len(colors)-1)
    texto =  colors[color]
    label = tkinter.Label(window, text=texto, bg=colors[color], fg=colors[color2])
    label.place(x=random.randint(0,300), y=random.randint(0,300))

window.mainloop()
