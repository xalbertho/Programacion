import math
import numpy as np


lista = (1,2,3, "Hola")

#lista[0] =9

print(lista)

dic = {'a': 1, 'b': "dos", 'a': 4}
dic['b'] = 8

print(dic)

set = {1,1,4,5,8,"hola"}
print(set)

x = float(10.5)
y = float(11)
z = float(12)
print(x)

cadena = 'Cadena de caracteres con un valor entero {:.2f},{},{} '
cadena2 = f"Hola {x:.2f}, {z}, {y}"

print(cadena.format(x,y,z))
print(cadena2)

datos = float(input("Usuario, escribe un numero: "))

if datos < 0:
    print("Mal")
else:    
    print(f"El numero es {datos:.2f} y su doble es {2*datos}")
    
for i in range(1,50,3):
    print(i)
else:
    print("FIN")
    
def suma(*vals:int)->int:
    """Hace una suma

    Args:
        a (int): Numero 1
        b (int): Numero 2

    Returns:
        int: La suma
    """
    resultado = 0
    for v in vals:
        resultado += v
    return resultado

print(suma(1,2,3,4,5,6,7,8,98,9))

multiplicacion = lambda a, b : a*b
print(multiplicacion(2,3))
