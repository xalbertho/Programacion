# crear una clase estudiante, la cual tenga los atributos de nombre, edad, grado
# metodos--> estudiar (el estudiante (nombre) esta estudiando)
# crear un objeto estudiante y isar el metodo estudiar()
# se debe interactuar con el usuario y este debe brindar los atributos

class Estudiante:
    def __init__(self, nombre,edad,grado):
        self.nombre=nombre
        self.edad=edad
        self.grado=grado
    def estudiando(self):
        print(f"El estudiante {self.nombre}, esta estudiando")

nombre=input("diga su nombre: ")
edad=int(input("Ingrese su edad: "))
grado=input("Ingrese su grado: ")

estudiante1=Estudiante(nombre,edad,grado);

print(f"""
        Datos del estudiante: \n\n
        nombre:{estudiante1.nombre}
        edad: {estudiante1.edad}
        grado: {estudiante1.grado}\n""")

while True:
    
    estudiar=input();

    if(estudiar.lower()=="estudiar"):
         estudiante1.estudiando()
        