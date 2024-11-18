'''
Barrios Mendez Jose Alberto
boleta: 2022640111
Practica 1
27/02/2024
'''

import os
import funciones

while True:
    try:

        print("Mi programa\n1.Media Aritmetica\n2. Desviacion estandar\n3. Burbuja\n4. Salir")
        opcion=int(input("Ingrese la opcion que desea: "))

        if opcion >0 and opcion <5:
            break;
        else: 
            os.system("cls")
    except ValueError:
        os.system("cls")
    
if opcion==1:
    os.system("cls")
    funciones.media()
if opcion==2:
    os.system("cls")
    funciones.desviacion_estandar()
if opcion==3:
    os.system("cls")
    funciones.burbuja()
if opcion==4:
    os.system("cls")
    print("Hata luego, vuelva pronto!!!!")
    exit()

