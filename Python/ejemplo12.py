
#ahora veremos algunos comandos para las tuplas
# tupla=es un arreglo el cual no se puede modificar una vez creado, esa es la diferencia a una lista
# algo importante para destacar es que en las listas como en las tuplas se pueden almacenar valores o datos que 
# no sean del mismo tipo

student=("Alberto",21,"male");

print(student.count("Alberto")); # metodo para contar cuantas veces aparece un elemento en una tupla
print(student.index("male"));

for x in student:
    print(x);

########
# notese que se puede buscar un valor en una tupla de esta forma

if "Alberto" in student:
    print("Alberto esta aqui");
else:
    print("nombre no encontrado")