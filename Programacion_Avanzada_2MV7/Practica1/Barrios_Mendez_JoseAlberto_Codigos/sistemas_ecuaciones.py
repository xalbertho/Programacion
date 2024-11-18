# resolver el sistema de ecuacaiones
'''
Barrios Mendez Jose Alberto
boleta: 2022640111
Practica 1
27/02/2024
'''

import numpy as num
import os
print("2x-4y-3z=15\n1x+5y-5z=5\n3x+2y+67z\n")
A=num.array([[2,-4,-3],[1,5,-5],[4,2,67]])
B=num.array([15,5,20])

A_inversa=num.linalg.inv(A)
X=num.dot(A_inversa,B)
print(f"Los resultados son:\nX={X[0]}\nY={X[1]}\nZ={X[2]}")

#haciendo la comprobacion
print("\nHaciendo la comprobacion A*X, lo que nos debe arrojar B")
print(num.dot(A,X))


while True: 
    opcion=input("Quieres resolver un sistema de ecuaciones de 3*3 (s/n)?: ")
    if opcion.lower()=="s":
        break
    elif opcion.lower()=="n":
        exit()
    else:
        os.system("cls")


matriz=num.zeros((3,3))
for i in range(3):
    for j in range(3):
        while True:
            try:
                matriz[i][j]=float(input(f"Ingrese el elemento [{i+1}][{j+1}] de la matriz: "))
                break
            except ValueError:
                os.system("cls")
                print("Ingresa un valor VALIDO!!!!")
        
resultados=num.zeros(3)

for i in range(3):
    while True:
        try: 
            resultados[i]=float(input(f"Ingrese el resultado de la ecuacion {i+1}: "))
            break
        except ValueError:
            os.system("cls")
            print("Ingrese un valor valido!!! ")
        except:
            pass

mat_inversa=num.linalg.inv(matriz)
resul=num.dot(mat_inversa,resultados)
print(f"La solucion a la ecuacion es:\nx={resul[0]}\ny={resul[1]}\nz={resul[2]}")
