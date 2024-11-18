class Producto:
    def __init__(self, nombre: str, precio: float, tiempo: float) -> None:
        self._nombre = nombre
        self._precio = precio
        self._tiempo_espera = tiempo

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def precio(self) -> float:
        return self._precio

    @property
    def tiempo_espera(self) -> float:
        return self._tiempo_espera

    def __str__(self) -> str:
        return f"{self.nombre}: Precio ${self.precio:.2f}, Tiempo de espera {self.tiempo_espera} min"

class Sodas(Producto):
    def __init__(self, nombre: str, precio: float) -> None:
        super().__init__(nombre, precio, 0)

class Mexicano(Producto):
    def __init__(self, nombre: str, precio: float) -> None:
        super().__init__(nombre, precio, 15)

class Rapido(Producto):
    def __init__(self, nombre: str, precio: float) -> None:
        super().__init__(nombre, precio, 7)

class Llenador(Producto):
    def __init__(self, nombre: str, precio: float) -> None:
        super().__init__(nombre, precio, 10)
class Postres(Producto):
    def __init__(self, nombre: str, precio: float) -> None:
        super().__init__(nombre, precio, 3)
class Sandwich(Producto):
    def __init__(self, nombre: str, precio: float) -> None:
        super().__init__(nombre, precio, 8)

class AguaBo(Sodas):
    def __init__(self) -> None:
        super().__init__("Agua Bonafont 1.5 L", 17.00)

class AguaSabor(Sodas):
    def __init__(self) -> None:
        super().__init__("Agua de Sabor 1L", 25.00)

class Malteada(Sodas):
    def __init__(self) -> None:
        super().__init__("Malteada", 38.00)

class SodaItaliana(Sodas):
    def __init__(self) -> None:
        super().__init__("Soda Italiana", 35.00)

class Carlota(Postres):
    def __init__(self) -> None:
        super().__init__("Carlota Limon", 20.00)

class Arroz(Postres):
    def __init__(self) -> None:
        super().__init__("Arroz con leche", 15.00)

class Flan(Postres):
    def __init__(self) -> None:
        super().__init__("Flan de caramelo", 15.00)

class Hot_Cakes(Postres):
    def __init__(self) -> None:
        super().__init__("Hot cakes dollar", 25.00)
class Gelatina(Postres):
    def __init__(self) -> None:
        super().__init__("Gelatina de mosaico", 15.00)

class Wafles(Postres):
    def __init__(self) -> None:
        super().__init__("Wafles 2 piezas", 2.00)

class Chilaquiles_(Mexicano):
    def __init__(self) -> None:
        super().__init__("Chilaquiles sencillos", 25)

class Chilaquiles_p(Mexicano):
    def __init__(self) -> None:
        super().__init__("Chilaquiles con pollo", 25)

class Molletes(Mexicano):
    def __init__(self) -> None:
        super().__init__("Molletes", 20)

class Sincronizada(Mexicano):
    def __init__(self) -> None:
        super().__init__("Sincronizada doble", 25)
class Nachos(Mexicano):
    def __init__(self) -> None:
        super().__init__("Nachos con queso", 25)

class Tacos_ahogados(Mexicano):
    def __init__(self) -> None:
        super().__init__("Tacos ahogados", 35)

class Fruta(Rapido):
    def __init__(self) -> None:
        super().__init__("Fruta picada",20)

class Verdura(Rapido):
    def __init__(self) -> None:
        super().__init__("Verdura",25)

class Cereal_S(Rapido):
    def __init__(self) -> None:
        super().__init__("Cereal sencillo",12)
class Cereal_Acom(Rapido):
    def __init__(self) -> None:
        super().__init__("Cereal acompañado",25)
class Chapata(Llenador):
    def __init__(self) -> None:
        super().__init__(nombre="Chapata", precio=32)
class Hojaldra(Llenador):
    def __init__(self) -> None:
        super().__init__(nombre="Hojaldra", precio=20)

class Pizza(Llenador):
    def __init__(self) -> None:
        super().__init__(nombre="Pizza Peperoni", precio=25)

class Hamburgesa(Llenador):
    def __init__(self) -> None:
        super().__init__(nombre="Hamburguesa de res", precio=35)
class Sopa(Llenador):
    def __init__(self) -> None:
        super().__init__(nombre="Sopa fria", precio=30)

class Sandich_P(Sandwich):
    def __init__(self)->None:
        super().__init__(nombre="Sandiwch de pollo",precio=28)

class Sandich_J(Sandwich):
    def __init__(self)->None:
        super().__init__(nombre="Sandiwch de jamon",precio=28)

class Sandich_H(Sandwich):
    def __init__(self)->None:
        super().__init__(nombre="Sandiwch de huevo duro",precio=28)

class Sandich_O(Sandwich):
    def __init__(self)->None:
        super().__init__(nombre="Sandiwch de otros guisos",precio=32)

class Pedido:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.items = []

    def agregar_item(self, item: Producto):
        self.items.append(item)

    def calcular_costo_total(self) -> float:
        return sum(item.precio for item in self.items)

    def calcular_tiempo_total(self) -> float:
        return sum(item.tiempo_espera for item in self.items)

    def obtener_lista_productos(self) -> str:
        productos_str = ""
        for item in self.items:
            productos_str += f"{item.nombre} ---- ${item.precio:.2f}\n"
        return productos_str

    def obtener_costo_total(self) -> str:
        return f"${self.calcular_costo_total():.2f}"

    def obtener_tiempo_total(self) -> str:
        return f"{self.calcular_tiempo_total()}"