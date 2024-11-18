class Persona:
    def __init__(self, nombre, edad, estatura, telefono):
        self.nombre = nombre
        self.edad = edad
        self.estatura = estatura
        self.telefono = telefono
        self.anio_nacimiento = 2024 - edad  

    def __str__(self):
        return f"¡Hola!, Mi nombre es {self.nombre}, tengo {self.edad} años, nací en {self.anio_nacimiento}, " \
               f"mido {self.estatura} metros y mi número de contacto es {self.telefono} ¡Saludos!"

# Crear una lista de Personas
personas = []

# Solicitar datos de 3 personas
for i in range(3):
    nombre = input(f"Ingrese el nombre de la persona {i+1}: ")
    edad = int(input(f"Ingrese la edad de {nombre}: "))
    estatura = float(input(f"Ingrese la estatura de {nombre} (en metros): "))
    telefono = input(f"Ingrese el número telefónico de {nombre}: ")
    persona = Persona(nombre, edad, estatura, telefono)
    personas.append(persona)

# Mostrar datos de las personas
for i, persona in enumerate(personas):
    print(f"Persona {i+1}:")
    print(persona)