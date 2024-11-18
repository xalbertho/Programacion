# ahora veremos algunos metodos para archivos en el sistemas
import os

path="E:\\prueba.txt"

if os.path.exists(path):
    print("Esta locacion existe")
    if os.path.isfile(path):
        print("Tha is  a file");
    