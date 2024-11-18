cadena = "Hola a todes"

x = 5
y = 3.4

cadena = "Variable 1 = {1:010.2f} y variable 0 = {0}"

print(cadena.format(x, y))

print(f"Variable x {x} y variable y {y:10.3f}")

edad = int(input("Usuario, ingresa tu edad: "))
print(f"Tu edad es {edad}")