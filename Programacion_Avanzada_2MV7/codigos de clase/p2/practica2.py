class Alumno:
    def __init__(self, nombre, apellido_paterno, apellido_materno, num_boleta, fecha_nacimiento, carrera, grupo, correo):
        self._nombre = nombre
        self._apellido_paterno = apellido_paterno
        self._apellido_materno = apellido_materno
        self._num_boleta = num_boleta
        self._fecha_nacimiento = fecha_nacimiento
        self._carrera = carrera
        self._grupo = grupo
        self._correo = correo

class Profesor:
    def __init__(self, nombre_completo, num_empleado):
        self._nombre_completo = nombre_completo
        self._num_empleado = num_empleado

class Lista:
    def __init__(self, profesor, alumnos):
        self._profesor = profesor
        self._alumnos = alumnos

    def mostrar_lista(self):
        print(f'Profesor: {self._profesor._nombre_completo}')
        print(f'No. Empleado: {self._profesor._num_empleado}')
        print('================================')
        print('Lista de Alumnos Inscritos')
        print('================================')
        for i, alumno in enumerate(self._alumnos, 1):
            print(f'{i}. {alumno._apellido_paterno} {alumno._apellido_materno}, {alumno._nombre} - {alumno._num_boleta} - {alumno._fecha_nacimiento} - {alumno._carrera} - {alumno._grupo} - {alumno._correo}')
        print('================================')
        print(f'Total de alumnos inscritos: {len(self._alumnos)}')


nombre_profesor = input("Ingrese el nombre completo del profesor: ")
num_empleado = input("Ingrese el número de empleado del profesor: ")
profesor = Profesor(nombre_profesor, num_empleado)

alumnos = []

while True:
    continuar = input("¿Desea ingresar un nuevo alumno? (s/n): ")
    if continuar.lower() != 's':
        break

    nombre = input("Ingrese el nombre del alumno: ")
    apellido_paterno = input("Ingrese el apellido paterno del alumno: ")
    apellido_materno = input("Ingrese el apellido materno del alumno: ")
    num_boleta = input("Ingrese el número de boleta del alumno: ")
    fecha_nacimiento = input("Ingrese la fecha de nacimiento del alumno (dd/mm/aaaa): ")
    carrera = input("Ingrese la carrera del alumno: ")
    grupo = input("Ingrese el grupo del alumno: ")
    correo = input("Ingrese el correo electrónico del alumno: ")

    alumno = Alumno(nombre, apellido_paterno, apellido_materno, num_boleta, fecha_nacimiento, carrera, grupo, correo)
    alumnos.append(alumno)

lista = Lista(profesor, alumnos)
lista.mostrar_lista()

# dia de muerteee
#examen de programacion orientada a obket¿s
'''
tiempo sin  tener un examen, idk if i am feeling'''

















