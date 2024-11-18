import os
from datetime import datetime

class Persona:
    def __init__(self,nombre,ap,am,fecha_n) -> None:
        self.nombre=nombre
        self.ap=ap
        self.am=am
        self.fecha_n=fecha_n
    
class Alumno(Persona):
    def __init__(self, nombre,ap,am,fecha_n,boleta,grupo,carrera,correo) -> None:
        super().__init__(nombre,ap,am,fecha_n)

        self.boleta=boleta
        self.grupo=grupo
        self.carrera=carrera
        self.correo=correo

    def __str__(self) -> str:
        return f"{self.ap} {self.am},{self.nombre}--{self.boleta}--{self.fecha_n}\n"\
        f"{self.carrera}--{self.grupo}--{self.correo}"

class Profesor(Persona):
    def __init__(self,nombre,no_empleado) -> None:
        super().__init__(nombre,ap=None,am=None,fecha_n=None)
        self.no_empleado=no_empleado

    def __str__(self) -> str:
        return f"\n\nProfesor:  {self.nombre}\nNo. Empleado: {self.no_empleado}"

   

def pedirnombre():
    while True:
        nombre=input("Ingrese el nombre: ")
        nombre_s_espacios=nombre.replace(" ","")
        if nombre_s_espacios.isalpha():
            break
        else:
            print("Ingrese un nombre valido!!")
    return nombre

def pedir_app_p():
    while True:
        apellido_p=input("Ingrese el Apellido PATERNO: ")
        apellido_s_espacios=apellido_p.replace(" ","")
        if apellido_s_espacios.isalpha():
            break
        else:
            print("Ingrese un apellido valido!!")
    return apellido_p

def pedir_app_m():
    while True:
        apellido_m=input("Ingrese el Apellido MATERNO: ")
        apellido_s_espacios=apellido_m.replace(" ","")
        if apellido_s_espacios.isalpha():
            break
        else:
            print("Ingrese un apellido valido!!")
    return apellido_m

def fecha_nacimiento():
      while True:
        fecha_nacimiento = input("Ingrese la fecha de nacimiento (DD/MM/AAAA): ")
        try:
            fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%d/%m/%Y")
            
            return fecha_nacimiento
        except ValueError:
            print("Formato de fecha incorrecto. Intente de nuevo.")

def pedir_boleta():
    while True:
        try:
            boleta=int(input("Ingrese el numero de boleta: "))
            break
        except ValueError:
            print("ingrese un numero de boleta valido!!! ")
    return boleta

def pedir_grupo():
    grupo=input("Ingrese su grupo: ")
    return grupo

def pedir_carrera():
    carrera=input("Ingrese su carrera: ")
    return carrera

def pedir_correo():
    while True:
        correo=input("Ingrese su correo electronico: ")
        if( '@' in correo):
            break
        else:
            print("Ingrese un correo electronico valido ")
    return correo

def pedir_no_empleado():
    while True:
        try:
            numero=int(input("Ingrese el numero de empleado: "))
            break
        except ValueError:
            print("ingrese un numero  de empleado valido!!! ")
    return numero



lista=[]
i=0
os.system("cls")

print("\n\n-----Datos del Profesor------")
profe=Profesor(pedirnombre(),pedir_no_empleado())

while True:
    os.system("cls")
    print(f"---------ALUMNO {i+1}------------")
    alumno = Alumno(pedirnombre(), pedir_app_p(), pedir_app_m(), fecha_nacimiento(), pedir_boleta(), pedir_grupo(), pedir_carrera(), pedir_correo())
    lista.append(alumno)
    respuesta = input("¿Desea agregar otro alumno a la lista? (s/n)")
    i += 1
    if respuesta.lower() == 'n':
        break
    elif respuesta.lower() == 's':
        continue
    else:
        print("Respuesta no válida. Por favor, responda 's' para sí o 'n' para no.")

os.system("cls")


print(profe)
print("-"*50)
print("Lista de alumnos")
print("-"*50)


for i in range(len(lista)):
    print(lista[i])
    print("-"*50)

print(f"Total de alumnos inscritos: {len(lista)}")






