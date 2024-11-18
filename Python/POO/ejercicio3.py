'''
EJERCICIO DE HERENCIA MULTIPLE MRO

Imagina que estas modelando aninales en un zoologico. Crear 3 clases
"Animal", "Mamifero" y "Ave". La clase Animal debe tener un metodo llamado comer
La clase Mamifere debe tener un metodo llamado amamantar y la clase ave un metodo llamado volar

Ahora crea una clase Murcielago que herede de mamifero y Ave, en ese orden, y por lo tanto
debe ser capar de amamantar y volar, ademas de comer

Finalmente, juega con el orden de herencia de la clase Murcielago y observa como cambia el c
comportamiento de los metodos al usar super

'''

class Animal:
    def comer(self):
        print("Animal comiendo...")

class Ave(Animal):
    def volar(self):
        print("Volando...")

class Mamifero(Animal):
    def amamantar(self):
        print("Amamantando...")

class Murielago(Ave,Mamifero):
    pass

mascota=Murielago();

mascota.volar()
mascota.amamantar()
mascota.comer()
