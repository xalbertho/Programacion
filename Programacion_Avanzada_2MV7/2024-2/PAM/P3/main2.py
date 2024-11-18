class Clase:
    deClase = 0
    
    def __init__(self) -> None:
        self.deInstancia = 0
    
    #De instancia
    def suma(self, a, b):
        return a+b
    
    @classmethod
    def resta(cls, a, b):
        return a - b
    
    @staticmethod
    def mult(a,b):
        return a*b
        
Clase.mult(5,6) 
Clase.deClase = 10
Clase.resta(4,5)
objeto = Clase()
objeto.deInstancia
objeto.deClase = 12
objeto.suma(2,3)  

print(Clase.deClase)