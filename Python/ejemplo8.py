
#ciclo for en python es de una forma 

x=int(input("Ingrese un numero del 1 al 10: "));
#la funcion in range, crea una secuencia de valores desde o hasta el valor o rango de x

for i in range(x):
    print(i);

#tambien podemos iterar sobre una tupla o dupla
#tupla= Una tupla es una colección inmutable, lo que significa que una vez creada, no se puede modificar, agregar ni eliminar elementos.
#       Se define utilizando paréntesis ().
#       Ejemplo: tupla = (1, 2, 'hola', True)
# lista=Una lista es una colección mutable, lo que significa que puedes modificar, agregar y eliminar elementos después de que la lista ha sido creada.
#       Las listas se pueden modificar utilizando métodos como append(), insert(), remove(), pop(), extend(), sort(), etc.
#Ejemplo: lista = [1, 2, 'hola', True]

lista1=[1,2,3,4,5,5,6,7];
for i in tuple(lista1):
    print(i);

for i in list(lista1[:5]):
    print(i);

for i in range(20,100,10):
    print(i);