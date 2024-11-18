# herencia= permite tener una clase hija que tiene todos los metodos
# y atributos de la clase padre, y tambien agregarle nuevos atributos
# para este caso nuestra clase padre va a ser la class Persona, ya que un empleado es una Persona, la clase de tipo empleado
# contiene todos los atributos y metodos de la class Persona
# para crear una class hija, basta con pasar como argumento la clase padre, asi de esta forma tendra todos los atributos

class Persona:
    def __init__(self, nombre,edad,nacionalidad,):
        self.nombre=nombre
        self.edad=edad
        self.nacionalidad=nacionalidad
    def hablar(self):
        print("Hello everyone ")

class Empleado(Persona):
    def __init__(self,nombre,edad,nacionalidad,trabajo,salario):
        super().__init__(nombre,edad,nacionalidad)
        self.trabajo=trabajo
        self.salario=salario

roberto=Empleado("roberto",30,"Mecicano","ingeniero",1000)
print(roberto.trabajo);
roberto.hablar()