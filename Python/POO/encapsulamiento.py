# consiste en proteger los elementos de una clase
# lo que en c++ es el equivalente a private
# lo cual tendria como fin proteger ciertas cosas

class Miclase:
    def __init__(self):
        self._atrivuto_privado="valor" # privado
        self.__atrivuto_muy_privado="hola" 


objeto=Miclase()
print(objeto._atrivuto_privado)
print(objeto.__atrivuto_muy_privado)