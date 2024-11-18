import tkinter as tk
import random

def shake_window(window, widgets):
    original_x = window.winfo_x()
    original_y = window.winfo_y()

    for _ in range(10):  # Número de sacudidas
        x_offset = random.randint(-10, 10)
        y_offset = random.randint(-10, 10)
        window.geometry(f"+{original_x + x_offset}+{original_y + y_offset}")

        for widget in widgets:
            widget.place_configure(x=widget.winfo_x() + random.randint(-5, 5),
                                   y=widget.winfo_y() + random.randint(-5, 5))
        
        window.update()
        window.after(50)  # Milisegundos entre sacudidas

    window.geometry(f"+{original_x}+{original_y}")
    for widget in widgets:
        widget.place_configure(x=widget.winfo_x() - (widget.winfo_x() % 10),
                               y=widget.winfo_y() - (widget.winfo_y() % 10))

def on_button_click():
    if entry_user.get() == "" and entry_password.get() == "":
        label_error.config(text="Campos Vacíos")
        shake_window(root, widgets)
    elif entry_user.get() == "":
        label_error.config(text="Falta Usuario")
        shake_window(root, widgets)
    elif entry_password.get() == "":
        label_error.config(text="Falta Contraseña")
        shake_window(root, widgets)
    elif entry_user.get() == "Admin" and entry_password.get() == "123":
        label_error.config(text="Inicio de sesión correcto")
        # Aquí puedes agregar la lógica para abrir una nueva ventana o continuar
    else:
        label_error.config(text="Datos Incorrectos")
        shake_window(root, widgets)

root = tk.Tk()
root.geometry("300x200")

label_user = tk.Label(root, text="Usuario:")
label_user.place(x=50, y=30)
entry_user = tk.Entry(root)
entry_user.place(x=150, y=30)

label_password = tk.Label(root, text="Contraseña:")
label_password.place(x=50, y=70)
entry_password = tk.Entry(root, show="*")
entry_password.place(x=150, y=70)

button = tk.Button(root, text="Iniciar Sesión", command=on_button_click)
button.place(x=100, y=120)

label_error = tk.Label(root, text="", fg="red")
label_error.place(x=100, y=160)

widgets = [label_user, entry_user, label_password, entry_password, button, label_error]

root.mainloop()
