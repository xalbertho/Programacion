archivo = open("prueba.txt", "r")
contenido = archivo.read()

print(contenido)
archivo.close()


archivo = open("../../prueba.txt", "w")
archivo.write("Hola a todos\nAdios")
archivo.close()

