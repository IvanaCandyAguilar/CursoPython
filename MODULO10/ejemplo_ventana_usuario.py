import tkinter
from tkinter import ttk
window = tkinter.Tk()

window.columnconfigure(0, weight=1)
window.columnconfigure(0, weight=3)

user_name = ttk.Label(window,text='Username:')
user_name.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)

user_entry = ttk.Entry(window)
user_entry.grid(column=1, row=0, sticky= tkinter.E, padx=5, pady=5)


password= ttk.Label(window,text='Password:')
password.grid(column=0, row=1, sticky=tkinter.W, padx=5, pady=5)

password = ttk.Entry(window, show='*')
password.grid(column=1, row=1, sticky= tkinter.E, padx=5, pady=5)

login_button = ttk.Button(window, text='Login')
login_button.grid(column=1, row=3, sticky= tkinter.E, padx=5, pady=5)

window.mainloop()
