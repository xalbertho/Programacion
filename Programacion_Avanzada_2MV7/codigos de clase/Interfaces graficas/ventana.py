import tkinter as tk

venata=tk.Tk()
#venata.title("Mi primera interfaz")
venata.wm_title("Mi primera interfaz")
venata.wm_minsize(300,300)
etiqueta=tk.Label(master=venata,text="Hola gui")
etiqueta.pack()

boton=tk.Button(master=venata,text="Aceptar")
boton.pack()

venata.mainloop()
