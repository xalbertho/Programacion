from abc import ABCMeta, abstractmethod

class Figura(metaclass=ABCMeta):
    """Clase Abstracta

    Args:
        metaclass (_type_, optional): Nos permite crear una clase abstracta en Python. Defaults to ABCMeta.
    """
    @abstractmethod
    def area(self):
        """Metodo abstracto
        """
        pass
    
class Rectangulo(Figura):
    def __init__(self, base, altura) -> None:
        super().__init__()
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura

class Circulo(Figura):
    def __init__(self, radio) -> None:
        super().__init__() # Llama al constructor por defecto de la super clase
        self.radio = radio
        
    def area(self):
        """Implementacion del metodo abstracto

        Returns:
            _type_: _description_
        """
        return 3.14 * self.radio ** 2

cir = Rectangulo(5, 9)
print(cir.area())