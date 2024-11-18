
'''
 EJERCICIO DE HERENNCIA Y USO DE SUPER:

 Crea un sistema par una escuela. En este sistema, vamos a tener 2 clases principales
 Persona y Estudiante. La clase Persona tendra los atributos de nombre y edad y un metodo que imprima el nombre y la 
 edad de la persona. La clase Estudiante heredara de la clase Persona y tambien tendra un atributo adicional "grado"
 del estudiante.

 Utiliza super, en el metodo de inicializacion (init) para retulizar el codifo de la clase padre
 (Persona). Luego crea una instancia de la clase Estudiante e imprime sus atributos y utiliza sus metodos
 para asegurarte que funcione correctamente

'''

class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad

    def presentarse(self):
        print(f"Hola mi nombre es {self.nombre} y tengo {self.edad} años")

class Estudiante(Persona):
    def __init__(self,nombre,edad, grado):
        super().__init__(nombre,edad)
        self.grado=grado
    
    def mostrar_grado(self):
        print(f"Grado: {self.grado} ")
         

estudiante1=Estudiante("Jose Alberto",20,9)
estudiante1.presentarse()
estudiante1.mostrar_grado()
