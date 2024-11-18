import tkinter as tk

venata=tk.Tk()
#venata.title("Mi primera interfaz")
venata.wm_title("Mi primera interfaz")
venata.wm_minsize(300,300)
etiqueta=tk.Label(master=venata,text="Hola gui")
etiqueta.pack()

boton=tk.Button(master=venata,text="Aceptar")
boton.pack()

entrada=tk.Entry(master=venata,width=30,justify="center")
entrada.pack()

def clic(event):
    print("El mensaje es: "+entrada.get())

boton.bind("<Button-1>",clic)
venata.mainloop()
