"""
Ahora veremos un poco sobre herencia multiple, donde un objeto puede heredar
las propiedades de dos clases (padres distintas)

vamos a partir del objeto del ejerciio anterior, pero añadiremos una nueva clase 
la cual contenga herencia de 2 clases distintas, con el fin de analizar el estudio de estas mismas

algo a destacar es que podemos hacer un llamado de una funcion, por ejemplo en la clase empleadoartista
puedo usar super() para mostrar la habilidad que tiene, sin ema¿bargo, esto mostrara la habilidad de la clase
padre, y por mas que se reescriba el metodo, siempre mostrara el de la clase padre, por otro lado, si usamos self
llamando a la funcion, se podra reescribit el metodo, y mostrar una habilidad diferente
"""

class Persona:
    def __init__(self, nombre,edad,nacionalidad,):
        self.nombre=nombre
        self.edad=edad
        self.nacionalidad=nacionalidad

    def hablar(self):
        print(f"Hello everyone my name is {self.nombre} ")

class Artista:
    def __init__(self,habilidad):
        self.habilidad=habilidad

    def mostrar_habilidad(self):

        print(f"Mi habilidad es: {self.habilidad}")

class EmpleadoArtista(Persona,Artista):
    def __init__(self,nombre,edad,nacionalidad,habilidad,salario,empresa):
        Persona.__init__(self,nombre,edad,nacionalidad)
        Artista.__init__(self,habilidad)
        self.salario=salario
        self.empresa=empresa
    
    def presentarse(self):
# Aqui la diferencia entre usar self y super, self mostrara la habilidad para este objeto unicamente, sin embargo
# si usamos super, mostrara la habilidad de la clase padre, si sobre escribimos el metodo es mejor usar self
# con super, siempre accedemos a mostrar habilidad de la clase padre 
       albert.mostrar_habilidad()       
       print(f"Yo trabajo en la empresa {self.empresa} y tengo un salario de {self.salario}")   # aqui s
      #  return f'{self.mostrar_habilidad}'
    
albert=EmpleadoArtista("Alberto",20,"Mexicana","Nadota",200000,"si")

albert.hablar()
albert.presentarse()

herencia=issubclass(EmpleadoArtista,Artista)
print(herencia)
isinstance=isinstance(albert,Persona)
print(isinstance)