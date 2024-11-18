

class Alumno:
    def __init__(self,nombre:str,boleta:str,edad:int) -> None:
        self.__nombre="Alberto"
        self.__boleta=""
        self.__edad=0
    @property
    def nombre(self):
        return self.nombre
    


alumno1=Alumno("Alberto","202223023",20)
#Para acceder a una variable privada es necesario primero, modificarla o crearla fuera de la clase,
#de este nodo si intentamos acceder directameente desde fuera, no nos dejara acceder

#alumno1.__nombre="Alberto" --> de esta forma si podemos modificaf a la variable "Privada"


#print(alumno1.__nombre)