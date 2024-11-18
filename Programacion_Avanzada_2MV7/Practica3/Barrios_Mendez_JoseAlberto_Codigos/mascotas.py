from abc import ABCMeta, abstractmethod

class Mascota(metaclass=ABCMeta):
    def __init__(self,nombre,edad,dueño,tipo) -> None:
        self.__nombre=nombre
        self.__edad=edad
        self.__dueño=dueño
        self.__tipo=tipo
    
    @property
    @abstractmethod
    def dueño(self):
        pass

    @property
    @abstractmethod
    def nombre(self):
        pass

    @property
    @abstractmethod
    def tipo(self):
        pass

    @property
    @abstractmethod
    def edad(self):
        pass
 
    @property
    @abstractmethod
    def habla(self):
        pass

    @property
    @abstractmethod
    def __str__(self) -> str:
        pass

    @__str__.setter
    @abstractmethod
    def __str__(self,nuevo_ha) -> str:
        pass

class Domestica(Mascota):
    
    def __init__(self, nombre, edad, dueño, tipo,ternura) -> None:
        super().__init__(nombre, edad, dueño, tipo)
        self.__ternura=ternura
    
    @property
    @abstractmethod
    def factor_ternura(self):
        pass

    @factor_ternura.setter
    @abstractmethod
    def factor_ternura(self,nuevo_factor_ternura):
        pass

class Exotica(Mascota):
    def __init__(self, nombre, edad, dueño, tipo,peligro) -> None:
        super().__init__(nombre, edad, dueño, tipo)
        self.__peligro=peligro
    
    @property
    @abstractmethod

    def factor_peligro(self):
        pass
    @factor_peligro.setter
    @abstractmethod
    def factor_peligro(self,nuevo_factor_peligro):
        pass


class Gato(Domestica):

    def __init__(self, nombre, edad, dueño, tipo, ternura) -> None:
        super().__init__(nombre, edad, dueño, tipo, ternura)

    @property
    def dueño(self):
        return self.__dueño

    @property
    def nombre(self):
        return self._Mascota__nombre

    @property
    def tipo(self):
        return self.__tipo

    @property
    def edad(self):
        return self.__edad
    
    @property
    def factor_ternura(self):
        return self._Domestica__ternura

    @factor_ternura.setter
    def factor_ternura(self, nuevo_factor_ternura):
        self.__ternura = nuevo_factor_ternura
    
    def __str__(self) -> str:
        return f"Gato: {self._Mascota__nombre}, Edad: {self._Mascota__edad}, Dueño: {self._Mascota__dueño},Tipo: {self._Mascota__tipo}, Ternura: {self._Domestica__ternura}"
    
    @property
    def habla(self):
        return 'MIAU MIAU'


class Perro(Domestica):
    def __init__(self, nombre, edad, dueño, tipo, ternura) -> None:
        super().__init__(nombre, edad, dueño, tipo, ternura)

    @property
    def dueño(self):
        return self.__dueño

    @property
    def nombre(self):
        return self._Mascota__nombre

    @property
    def tipo(self):
        return self.__tipo

    @property
    def edad(self):
        return self.__edad
    
    @property
    def factor_ternura(self):
        return self._Domestica__ternura

    @factor_ternura.setter
    def factor_ternura(self, nuevo_factor_ternura):
        self.__ternura = nuevo_factor_ternura
    
    def __str__(self) -> str:
        return f"Gato: {self._Mascota__nombre}, Edad: {self._Mascota__edad}, Dueño: {self._Mascota__dueño}, Tipo: {self._Mascota__tipo}, Ternura: {self._Domestica__ternura}"
    
    @property
    def habla(self):
        return 'GUAO GUAO'


class Vivora(Exotica):
    def __init__(self, nombre, edad, dueño, tipo, peligro) -> None:
        super().__init__(nombre, edad, dueño, tipo, peligro) 
    
    @property
    def factor_peligro(self):
        return self.__peligro

    @factor_peligro.setter
    def factor_peligro(self,nuevo_factor_p):
        self.__peligro=nuevo_factor_p

    
    @property
    def dueño(self):
        return self.__dueño

    @property
    def nombre(self):
        return self._Mascota__nombre

    @property
    def tipo(self):
        return self.__tipo

    @property
    def edad(self):
        return self.__edad
    
    @property
    def habla(self):
        return 'tsss tssss'

    def __str__(self) -> str:
        return f"Vivora {self.habla}: {self._Mascota__nombre}, Edad: {self._Mascota__edad}, Dueño: {self._Mascota__dueño}, Tipo: {self._Mascota__tipo}, Peligro: {self._Exotica__peligro}"
    
class Tigre(Exotica):
    def __init__(self, nombre, edad, dueño, tipo, peligro) -> None:
        super().__init__(nombre, edad, dueño, tipo, peligro)
    
    @property
    def factor_peligro(self):
        return self.__peligro

    @factor_peligro.setter
    def factor_peligro(self,nuevo_factor_p):
        self.__peligro=nuevo_factor_p

    
    @property
    def dueño(self):
        return self.__dueño

    @property
    def nombre(self):
        return self._Mascota__nombre

    @property
    def tipo(self):
        return self.__tipo

    @property
    def edad(self):
        return self.__edad
    
    @property
    def habla(self):
        return 'Grrrr'

    def __str__(self) -> str:
        return f"Tigre {self.habla}: {self._Mascota__nombre}, Edad: {self._Mascota__edad}, Dueño: {self._Mascota__dueño}, Tipo: {self._Mascota__tipo}, Peligro: {self._Exotica__peligro}"
  
class Dinosaurio(Exotica):
    def __init__(self, nombre, edad, dueño, tipo, peligro) -> None:
        super().__init__(nombre, edad, dueño, tipo, peligro)


class Brontosaurio(Dinosaurio):
    def __init__(self, nombre, edad, dueño, tipo, peligro) -> None:
        super().__init__(nombre, edad, dueño, tipo, peligro)

    @property
    def factor_peligro(self):
        return self.__peligro

    @factor_peligro.setter
    def factor_peligro(self,nuevo_factor_p):
        self.__peligro=nuevo_factor_p

    
    @property
    def dueño(self):
        return self.__dueño

    @property
    def nombre(self):
        return self._Mascota__nombre

    @property
    def tipo(self):
        return self.__tipo

    @property
    def edad(self):
        return self.__edad
    
    @property
    def habla(self):
        return 'Hola soy un brontosaurio grrrrr'

    def __str__(self) -> str:
        return f"{self.habla}. Nombre: {self._Mascota__nombre}, Edad: {self._Mascota__edad}, Dueño: {self._Mascota__dueño}, Tipo: {self._Mascota__tipo}, Peligro: {self._Exotica__peligro}"

class Raptor(Dinosaurio):
    def __init__(self, nombre, edad, dueño, tipo, peligro) -> None:
        super().__init__(nombre, edad, dueño, tipo, peligro)

    @property
    def factor_peligro(self):
        return self.__peligro

    @factor_peligro.setter
    def factor_peligro(self,nuevo_factor_p):
        self.__peligro=nuevo_factor_p

    
    @property
    def dueño(self):
        return self.__dueño

    @property
    def nombre(self):
        return self._Mascota__nombre

    @property
    def tipo(self):
        return self.__tipo

    @property
    def edad(self):
        return self.__edad
    
    @property
    def habla(self):
        return 'Hola soy un Raptor '

    def __str__(self) -> str:
        return f"{self.habla}. Nombre:{self._Mascota__nombre}, Edad: {self._Mascota__edad}, Dueño: {self._Mascota__dueño}, Tipo: {self._Mascota__tipo}, Peligro: {self._Exotica__peligro}"
  
class TRex(Dinosaurio):
    def __init__(self, nombre, edad, dueño, tipo, peligro) -> None:
        super().__init__(nombre, edad, dueño, tipo, peligro)

    @property
    def factor_peligro(self):
        return self.__peligro

    @factor_peligro.setter
    def factor_peligro(self,nuevo_factor_p):
        self.__peligro=nuevo_factor_p

    
    @property
    def dueño(self):
        return self.__dueño

    @property
    def nombre(self):
        return self._Mascota__nombre

    @property
    def tipo(self):
        return self.__tipo

    @property
    def edad(self):
        return self.__edad
    
    @property
    def habla(self):
        return 'Hola, soy un Trex ggrgrgrgrgr'

    def __str__(self) -> str:
        return f"{self.habla}. Nombre: {self._Mascota__nombre}, Edad: {self._Mascota__edad}, Dueño: {self._Mascota__dueño}, Tipo: {self._Mascota__tipo}, Peligro: {self._Exotica__peligro}"
  

if __name__=='__main__':
    m1=Gato(nombre="asasda",edad=12,dueño="Alberto",tipo="Gato",ternura=5)
    print(m1.nombre)
    v1=Vivora(nombre="asasda",edad=12,dueño="Alberto",tipo="Gato",peligro=5)
    print(v1)
    t1=Tigre(nombre="asasda",edad=12,dueño="Alberto",tipo="Gato",peligro=5)
    print(t1)

    d1=Raptor(nombre="asasda",edad=12,dueño="Alberto",tipo="Gato",peligro=5)
    print(d1)


