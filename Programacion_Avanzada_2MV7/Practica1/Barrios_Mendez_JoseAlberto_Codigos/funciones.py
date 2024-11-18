'''
Barrios Mendez Jose Alberto
boleta: 2022640111
Practica 1
27/02/2024
'''

import os
import numpy as num


def solicitar_elementos():
 
    while True:
        try :
            num_elementos=int(input("Ingrese el numero de elementos a  ingresar: "))

            break
        except ValueError:
            os.system("cls")
            print("Ingresa un valor valido: ")
    return num_elementos
 
def media():
    
    num_elementos = solicitar_elementos() 
    mat=num.empty(num_elementos)
    
    suma=0
    
    for i in range(num_elementos):
        while True:
            try :
                mat[i]=float(input(f"Ingrese el elemento {i+1}: "))
                suma+=mat[i]
                break
            except ValueError:
                os.system("cls")
                print("Elemento no valido: ")
    print(suma/num_elementos)


def desviacion_estandar():
    
    elementos=solicitar_elementos()
    mat_elementos=num.empty(elementos)
    for i in range(elementos):

        while True:
            try:
                mat_elementos[i]=int(input(f"Ingrese el elemento {i+1}: "))
                break;
            except ValueError:
                os.system("cls")
                print("Elemento no valido, prueva con UN NUMERO: ")
                
    print("La desviacion estandar es: ",num.std(mat_elementos))  


def burbuja():
    num_elementos=solicitar_elementos()
    mat=num.random.rand(num_elementos)
    print(f"La matriz de {num_elementos} elementos aleatorios es:\n{mat}")

    for i in range(num_elementos):
        for j in range(num_elementos-i-1):
            if mat[j]>mat[j+1]:
                temp=mat[j+1]
                mat[j+1]=mat[j]
                mat[j]=temp
    print(f"El arreglo ordenado es: {mat}")


