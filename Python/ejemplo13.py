
# set= collecion desordenada de elementos unicos no indixados
# se pcupan cuando se desea almacenar elementos unicos sin tener en cuenta 
# el orden en que se agregaron
# NO PUEDE HABER ELEMEMENTOS DUPLICADOS

utensilios={"tenedor","cuchara","cuchillo"};
trastes={"plato","taza","copa"};


# utensilios.add("asd") metodo para añadir elementos al set
# utensilios.remove("tenedor") --> metodo para eliminar el elemento
# utensilios.clear() metodo para limpiar un set
mesa_cenar=utensilios.union(trastes); # metodo para union de conjuntos, si hay elementos repitivos solo toma uno
for j in mesa_cenar:
    print(j);

print("\n");
for x in utensilios:
    print(x);

#trastes.update(utensilios); # metodo para añadir un set a otro

#print("\n")
#for i in trastes:
 #   print(i);

print("\n");
print(utensilios.difference(trastes)); #diferencias
print(utensilios.intersection(trastes)); # mismos valores


