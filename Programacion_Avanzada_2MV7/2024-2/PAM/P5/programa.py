class Manzana:
    def __init__(self, color, tamanio) -> None:
        self.color = color
        self.tamanio = tamanio
    
    def __add__(self, manzana):
        mfinal = Manzana(self.color, self.tamanio + manzana.tamanio)
        return mfinal
        
    def __str__(self) -> str:
        return f"Color {self.color} y tamanio {self.tamanio}"

    def __gt__(self, manzana):
        return self.tamanio > manzana.tamanio
    
m1 = Manzana("Rojo", 5)
m2 = Manzana("Rojo", 3)

m3 = m1 + m2
print(m1>m2)