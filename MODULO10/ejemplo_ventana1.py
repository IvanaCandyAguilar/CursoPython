import tkinter

window = tkinter.Tk()
label_saludo = tkinter.Label(window,text='hola',bg='yellow',fg='blue')
#label_saludo.pack(ipadx=50, ipady=50, fill='x') #en fill pueden haber valores x,y,both
#label_saludo.pack(ipadx=50, ipady=50, expand=True)
label_saludo.pack(ipadx=30, ipady=30, side='left')


label_adios = tkinter.Label(window,text='adios', bg='red', fg='white')
#label_adios.pack(ipadx=50, ipady=100)
#label_adios.pack(fill='both', expand=True)
label_adios.pack(ipadx=30, ipady=30, side='right')
window.mainloop()
