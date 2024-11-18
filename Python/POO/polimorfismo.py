'''
polimorfismo= hace referencia a enviar algun tipo de informacion
este devuelva un valor distinto de acuerdo a sus propiedades de cada uno

por ejemplo, tenemos la clase animales, con metodo de "hablar"
y tenemos objetos como perro, gato, etc,
cada que enviemos o llamemos el metodo "hablar" cada objeto tendra un
resultado diferente

entendemos como polimorfismo a las distintas formas que puede tener un metodo dentro de cada objeto
El polimorfismo es una técnica de la programación orientada a objetos que 
permite a distintos objetos responder de manera diferente a un mismo llamado de método
'''

class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hacer_sonido(self):
        print("Este animal hace algún sonido")

# aqui la clase Perro hereda nombre,edad de la clase padere, ademas de agregar otro atribut (raza), tambien sobreescribe el metodo
#hacer sonido, el cual unicamente esta disponible para esta clase y no modifica la clase padre
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza

    def hacer_sonido(self):
        print("El perro hace guau guau")

mascota=Perro("El diputado",3,"golden")
mascota.hacer_sonido()