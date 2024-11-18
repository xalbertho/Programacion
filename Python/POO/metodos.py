 # los metodos son funciones dentro de una clase
class Celular:
    def __init__(self,marca,modelo,camara): #constructor. self hace referencia asi mismo
        self.marca=marca
        self.modelo=modelo
        self.camara=camara
    
    def llamar(self):
        print(f"Usted esta llamando desde un: {self.modelo}")

    def cortar(self):
        print(f"Esta terminando la llamada desde un: {self.modelo}")

celular1=Celular("samsung","s23","48 Mpx")
celular2=Celular("apple","11 pro","12 Mpx")

print(celular1.marca)
print(celular2.camara)
celular2.llamar()

