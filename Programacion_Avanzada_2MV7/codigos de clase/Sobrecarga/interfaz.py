from abc import ABCMeta, abstractmethod

class Figura(metaclass=ABCMeta):
    @abstractmethod
    def area(self):
        pass


class Circulo(Figura):
    def __init__(self,radio) -> None:
        super().__init__()
        self.radio=radio

    def area(self):
        return 3.14*self.radio**2
    

circ=Circulo(5);
print(circ.area)