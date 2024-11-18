
class Contacto:
    def __init__(self,nombre,telefono):
        self.__nombre=nombre
        self.__telefono=telefono
    
    def __str__(self) -> str:
        return f"nombre: {self.__nombre}, telefono: {self.__telefono}"
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def telefono(self):
        return self.__telefono
    

class Agenda:
    def __init__(self):
        self.__agenda=[]
    
    def agregar(self,contacto):
        self.__agenda.append(contacto)
    
    def eliminar(self,contacto):
        self.__agenda.remove(contacto)

    def buscar(self,nombre):
        
        for i in self.__agenda:
            if i.nombre==nombre:
                print(f"El contacto {i.nombre} con numero {i.telefono} esta en la lista")
            
            else:
                print(f"El contacto con nombre: {nombre} no esta en lista...")
                
    
    def buscar_t(self,telefono):
        for i in self.__agenda:
            if i.telefono==telefono:
                print(f"El contacto {i.nombre} con numero {i.telefono} esta en la lista")
                
            else:
                print(f"El contacto con numero: {telefono} no esta en lista...")

    def imprimir(self):
        print("Contactos guardados: ")
        for i in self.__agenda:
            print(i)

        