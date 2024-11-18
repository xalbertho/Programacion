class Alumno:
    def __init__(self, nombre, apellido_paterno, apellido_materno, numero_boleta, fecha_nacimiento, carrera, grupo, correo):
        self._nombre = nombre
        self._apellido_paterno = apellido_paterno
        self._apellido_materno = apellido_materno
        self._numero_boleta = numero_boleta
        self._fecha_nacimiento = fecha_nacimiento
        self._carrera = carrera
        self._grupo = grupo
        self._correo = correo

    @property
    def nombre_completo(self):
        return f"{self._apellido_paterno} {self._apellido_materno}, {self._nombre}"

    def __str__(self):
        return f"{self.nombre_completo} - {self._numero_boleta} - {self._fecha_nacimiento} - {self._carrera} - {self._grupo} - {self._correo}"

class Profesor:
    def __init__(self, nombre_completo, numero_empleado):
        self._nombre_completo = nombre_completo
        self._numero_empleado = numero_empleado

    @property
    def nombre_completo(self):
        return self._nombre_completo

    @property
    def numero_empleado(self):
        return self._numero_empleado
    

class Lista:
    def __init__(self, profesor):
        self._profesor = profesor
        self._alumnos = []

    def agregar_alumno(self, alumno):
        self._alumnos.append(alumno)

    def imprimir_lista(self):
        print(f"Profesor: {self._profesor.nombre_completo}")
        print(f"No. Empleado: {self._profesor.numero_empleado}")
        print("================================")
        print("Lista de Alumnos Inscritos")
        print("================================")
        for i, alumno in enumerate(self._alumnos, start=1):
            print(f"{i}. {str(alumno)}")
        print("================================")
        print(f"Total de alumnos inscritos: {len(self._alumnos)}")

def validar_entrada(mensaje, tipo_dato):
    while True:
        try:
            entrada = tipo_dato(input(mensaje))
            return entrada
        except ValueError:
            print(f"Error: Entrada inválida. Por favor, ingrese un valor de tipo {tipo_dato.__name__}.")

# Capturar datos del profesor
nombre_completo_profesor = input("Ingrese el nombre completo del profesor: ")
numero_empleado_profesor = validar_entrada("Ingrese el número de empleado del profesor: ", int)
profesor = Profesor(nombre_completo_profesor, numero_empleado_profesor)

# Crear la lista de alumnos
lista_alumnos = Lista(profesor)

# Capturar datos de los alumnos
continuar = True
while continuar:
    nombre = input("Ingrese el nombre: ")
    apellido_paterno = input("Ingrese el apellido paterno: ")
    apellido_materno = input("Ingrese el apellido materno: ")
    numero_boleta = input("Ingrese el número de boleta: ")
    fecha_nacimiento = input("Ingrese la fecha de nacimiento (dd/mm/aaaa): ")
    carrera = input("Ingrese la carrera: ")
    grupo = input("Ingrese el grupo: ")
    correo = input("Ingrese el correo electrónico: ")
    alumno = Alumno(nombre, apellido_paterno, apellido_materno, numero_boleta, fecha_nacimiento, carrera, grupo, correo)
    lista_alumnos.agregar_alumno(alumno)

    respuesta = input("¿Desea ingresar otro alumno? (s/n): ").lower()
    if respuesta != "s":
        continuar = False

# Imprimir la lista de alumnos
lista_alumnos.imprimir_lista()