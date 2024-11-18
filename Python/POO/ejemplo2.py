# ahora veremos los atributos, que son las variables de las clases 
# def se va a ejecutar cada que creamos una isntancia de celular y le pasamos los argumentos
# def es un constructor, crea las variables o atributos de acuerdo a los valores dados


class Celular:
    def __init__(self,marca,modelo,camara): #constructor. self hace referencia asi mismo
        self.marca=marca
        self.modelo=modelo
        self.camara=camara

celular1=Celular("samsung","s23","48 Mpx")
celular2=Celular("apple","11 pro","12 Mpx")
print(celular1.marca)
print(celular2.marca)



