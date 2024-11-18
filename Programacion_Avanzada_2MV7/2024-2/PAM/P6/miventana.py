import tkinter as tk
import tkinter.messagebox as msgbox

def click2():
    #print("El mensaje es: " + entrada.get())
    if msgbox.askyesno("Pregunta", "Le entendiste?"):
        msgbox.showinfo("Felicidades", "Me da gusto")
    else:
        msgbox.showerror("Chales", "Tu muy mal")


ventana = tk.Tk()

ventana.wm_title("Mi primer ventana")
ventana.wm_minsize(300, 300)
etiqueta = tk.Label(master=ventana,text="Nombre:")
etiqueta.pack(expand=True)
entrada = tk.Entry(master=ventana, width=30, justify="center")
entrada.pack(expand=True)
boton = tk.Button(master=ventana, text="Aceptar", command=click2, background="red")
boton.pack(fill=tk.BOTH, expand=True)


def click(event):
    print("El mensaje es: " + entrada.get())
    
#boton.bind("<Button-1>", click)

ventana.mainloop()