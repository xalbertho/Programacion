class Pelicula:
    def __init__(self,titulo,año,duracion,clasificacion,director,actores,descripcion):
        self.__titulo=titulo
        self.__año=año
        self.__duracion=duracion
        self.__clasificacion=clasificacion
        self.__director=director
        self.__actores=actores
        self.__descpricion=descripcion

    def __str__(self) -> str:
        return f"Pelicula:\nTitulo: {self.__titulo}, Año: {self.__año}, duracion: {self.__duracion}, clasificacion: {self.__director},\n actores: {self.__actores}, descpripcion: {self.__descpricion}"
    

class Catalogo:
    def __init__(self) :
        self._pelicula=[]

    def imprimir_catalogo(self):
        print("El catalogo de peliculas es el siguiente: ")
        for i in range(len(self._pelicula)):
            print("\n")
            print(self._pelicula[i])
            print("\n")

    def agregar(self,pelicula):
        self._pelicula.append(pelicula)



