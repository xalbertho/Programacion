from mascotas import Gato,Perro,Tigre,Vivora,Brontosaurio,TRex,Raptor
import os
from prettytable import PrettyTable

def imprimir_menu():
    menu = PrettyTable()
    menu.field_names = ["Opción", "Descripción"]
    menu.add_row(["1", "Adquirir mascota"])
    menu.add_row(["2", "Visualizar mascotas"])
    menu.add_row(["3", "Salir"])
    return menu


def imprimir_menu2():
    menu = PrettyTable()
    menu.field_names = ["Tipo de mascota", "Número", "Especies disponibles"]

    especies_domesticas = [
        ("Perro", 1),
        ("Gato", 2)
    ]

    especies_exoticas = [
        ("Vívora", 3),
        ("Tigre", 4),
        ("Dinosaurio (Brontosaurio)", 5),
        ("Dinosaurio (Raptor)", 6),
        ("Dinosaurio (TRex)", 7)
    ]

    for especie, numero in especies_domesticas:
        menu.add_row(["Domésticas" if numero == 1 else "", numero, especie])

    for especie, numero in especies_exoticas:
        menu.add_row(["Exóticas" if numero == 3 else "", numero, especie])

    return menu

 

def obtener_nombre():
    return input("Ingrese el nombre: ")

def obtener_edad():
    while True:
        try:
            edad = int(input("Ingrese la edad: "))
            if edad < 0:
                raise ValueError("La edad debe ser un número positivo.")
            return edad
        except ValueError:
            print("Error: Ingrese un número válido para la edad.")

def obtener_dueño():
    return input("Ingrese el nombre del dueño: ")

def obtener_nivel_ternura():
    while True:
        try:
            nivel = int(input("Ingrese el nivel de ternura (0 a 10): "))
            if nivel <0 or nivel>10 :
                print("El nivel debe estar en el rango.")
            else:
                return nivel
        except ValueError:
            print("Error: Ingrese un número válido para el nivel.")

def obtener_nivel_peligro():
    while True:
        try:
            nivel = int(input("Ingrese el nivel de peligro (0 a 10): "))
            if nivel <0 or nivel>10 :
                print("El nivel debe estar en el rango.")
            else:
                return nivel
        except ValueError:
            print("Error: Ingrese un número válido para el nivel.")

def obtener_tipo():
    return input("Ingrese el tipo: ")

print("\n\n¡Bienvenido al sistema de adopción de mascotas!")



def obtener_opcion(mensaje, maximo):
    while True:
        try:
            opcion = int(input(mensaje))
            if 1 <= opcion <= maximo:
                return opcion
            else:
                print(f"Por favor, ingresa un número entre 1 y {maximo}.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

lista=[]
import os

def obtener_opcion(mensaje, maximo):
    while True:
        try:
            opcion = int(input(mensaje))
            if 1 <= opcion <= maximo:
                return opcion
            else:
                print(f"Por favor, ingresa un número entre 1 y {maximo}.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

while True:
    print(imprimir_menu())
    opcion = obtener_opcion("\nIngrese una opcion: ", 3)
    os.system("cls")

    if opcion == 1:
        print("A continuación, las mascotas disponibles:")
        print(imprimir_menu2())
        op2 = obtener_opcion("Seleccione la mascota que desea adoptar: ", 7)
        os.system("cls")

        if op2 == 1:
            mascota = Perro(nombre=obtener_nombre(), edad=obtener_edad(), dueño=obtener_dueño(), ternura=obtener_nivel_ternura(), tipo=obtener_tipo())
        elif op2 == 2:
            mascota = Gato(nombre=obtener_nombre(), edad=obtener_edad(), dueño=obtener_dueño(), ternura=obtener_nivel_ternura(), tipo=obtener_tipo())
        elif op2 == 3:
            mascota = Vivora(nombre=obtener_nombre(), edad=obtener_edad(), dueño=obtener_dueño(), peligro=obtener_nivel_peligro(), tipo=obtener_tipo())
        elif op2 == 4:
            mascota = Tigre(nombre=obtener_nombre(), edad=obtener_edad(), dueño=obtener_dueño(), peligro=obtener_nivel_peligro(), tipo=obtener_tipo())
        elif op2 == 5:
            mascota = Brontosaurio(nombre=obtener_nombre(), edad=obtener_edad(), dueño=obtener_dueño(), peligro=obtener_nivel_peligro(), tipo=obtener_tipo())
        elif op2 == 6:
            mascota = Raptor(nombre=obtener_nombre(), edad=obtener_edad(), dueño=obtener_dueño(), peligro=obtener_nivel_peligro(), tipo=obtener_tipo())
        elif op2 == 7:
            mascota = TRex(nombre=obtener_nombre(), edad=obtener_edad(), dueño=obtener_dueño(), peligro=obtener_nivel_peligro(), tipo=obtener_tipo())

        lista.append(mascota)
        print("Mascota agregada con exito")


    elif opcion == 2:
        print('-'*60)
        print("MASCOTAS ADQUIRIDAS")
        print('-'*60)
        for i in range(len(lista)):
            print(lista[i])
        input("Presione cualquier tecla para regresar al menú principal.")
        os.system("cls")

    elif opcion == 3:
        print("Hasta la proxima!!! ")
        break