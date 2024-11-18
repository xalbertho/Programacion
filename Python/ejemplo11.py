#lista= una lista es un arreglo que se puede modificar añadiendo datos etc...

lista1=["pasta","pizza","tacos"];


for i in list(lista1): #tambien se puede imprimir de la fotma for i in lista1
    print(i);

lista1.append("Pasas"); #metodo para añadir elementos a una lista
lista1.remove("pasta"); #metodo para eliminar elementos de una lista

print("\n");

for i in list(lista1): #tambien se puede imprimir de la fotma for i in lista1
    print(i);

print("\n");
lista1.pop(); #metodo para eliminar el ultimo elemento de la lisma
for i in list(lista1): #tambien se puede imprimir de la fotma for i in lista1
    print(i);
print("\n");
lista1.insert(0,"Galletas");  #metodo para insertar un elemento en un aubicacion deseada
for i in list(lista1): #tambien se puede imprimir de la fotma for i in lista1
    print(i);

print("\n");
lista1.sort(); # metodo para ordenar los elementos de una lista, si son numeros, los ordena de menor a mayor, en caso de 
                # que se trate de un string, lo ordenara por orden alfabetico

for i in list(lista1): 
    print(i);

print("\n");
lista1.clear(); #---metodo para limpiar una lista
for i in list(lista1): #tambien se puede imprimir de la fotma for i in lista1
    print(i);