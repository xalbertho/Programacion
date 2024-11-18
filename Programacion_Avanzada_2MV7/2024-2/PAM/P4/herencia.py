class Persona:

    def __init__(self, nombre: str, edad: int) -> None:
        self.__nombre = nombre
        self.__edad = edad

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad: int):
        self.__edad = edad

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevoNombre: str):
        if len(nuevoNombre) != 0:
            self.__nombre = nuevoNombre

class Alumno(Persona):
    pass
    
        

alu = Alumno("N", 0)

    
    