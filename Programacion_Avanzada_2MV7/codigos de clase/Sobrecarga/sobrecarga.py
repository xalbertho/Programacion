'''
Sobrecarga de operadores, 

'''
class Manzanas:
    def __init__(self,color,tamaño) -> None:
        self.color=color
        self.tamaño=tamaño
    
    def __add__(self,manzana):
        if(manzana.tamaño):
            mfinal=Manzanas(self.color,self.tamaño+manzana.tamaño)
            return mfinal
    
    def __str__(self) -> str:
        return f"color {self.color} y tamaño {self.tamaño}"

m1=Manzanas("Rojo",5)
m2=Manzanas("Verde",3)

print(m1+m2)