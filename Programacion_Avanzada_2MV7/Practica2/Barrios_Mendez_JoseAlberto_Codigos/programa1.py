'''
BARRIOS MENDEZ JOSE ALBERTO

Numero de boleta: 2022640111

'''
import numpy as num
import os

class Persona:
    def __init__(self,nombre,edad,estatura,telefono) -> None:
        self.nombre=nombre
        self.edad=edad
        self.estatura=estatura
        self.telefono=telefono
    
    def __str__(self) -> str:

        return f"!Hola¡, Mi nombre es {self.nombre}, tengo {self.edad} años, naci en {-self.edad+2024}\nmido" \
        f"{self.estatura} metros y ni numero de telefono es {self.telefono} !Saludos¡"
    
def pedir_nombre():
    while True:
        nombre=(input("Ingrese el nombre: "))

        if (nombre.isalpha()):
             break
        else:
            print("Ingresa un nombre valido!!")
    return nombre    
        


def pedir_edad():
    while True:
        try:
            edad=int(input("ingrese su edad: "))
            if (edad<=0 or edad>100):
                print("Ingrese una edad valida: ")
            else:
                break
        except ValueError:
            print("Ingrese una edad valida ")

    return edad

def pedir_estatura():
    while True:
        try:
            estatura=float(input("Ingrese su estatura en metros : "))
            if (estatura<=0 or estatura >2.15):
                print("Estatura no valida: ")
            else:
                break
        except ValueError:
            print("Estatura  invalida: ")
    
    return estatura

def pedir_telefono():
    while True:
        try:
            numero=int(input("Ingrese su numero de telefono (10 digitos): \n"))
            if (numero<0 or (len(str(numero))<10)):
                print("Ingres un numero valido")
            else :
                break
        except ValueError:
            print("Ingrese un numero valido: ")
    return numero




print("\n\n")



personas=[]

for i in range(3):
    print(f"--------PERSONA {i+1}")
    persona=Persona(pedir_nombre(),pedir_edad(),pedir_estatura(),pedir_telefono())
    personas.append(persona)
    os.system("cls")

os.system("cls")   
for i in range(3):
    print(personas[i])
