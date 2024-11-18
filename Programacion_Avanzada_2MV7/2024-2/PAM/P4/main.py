class Alumno:
    
    def __init__(self, nombre:str, boleta:str, edad:int) -> None:
        self.__nombre = nombre
        self.__boleta = boleta
        self.__edad = edad
    
    @property
    def boleta(self):
        return self.__boleta
    
    @boleta.setter
    def boleta(self, nuevaBoleta:str):
        self.__boleta = nuevaBoleta   
    
    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, edad:int):
        self.__edad = edad
    
    @property 
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevoNombre:str):
        if(len(nuevoNombre) != 0):
            self.__nombre = nuevoNombre
          
    
        
alumno1 = Alumno("Jose Luis", "202456779", 25)

alumno1.nombre = ""
print(alumno1.nombre)