
#slicing= create a substring by extracting elements from another string
#         indexing[] or slice()
#         [start:stop:step]
#en python nos va a permmitir extraer una parte especifica de una secuencia, como una cadena
# secuencia[inicio:fin:paso]
#

name="Alberto mendez";

first_name=name[:7]; #indicara que comienza desde el inicio de la cadena hasta el indice 7;
print(first_name);
lastname=name[8:]; #comienza desde el indice 8 hasya el final de la cadena

print(lastname);

random_name=name[::2]; #indica que comienza desde el inicio hasta el final con un paso de 2 posiciones
print(random_name);
#tambien puede aumntar en forma inversa es decir con paso negativo

website1="htpps://google.com";
website2="htpps://wikipedia.com";

slice=slice(7,-4) #indica que empieza en la posicon 7 del array, y termina en la posicion -4, osea
#                  que debemos contar del final
print(website1[slice]);
print(website2[slice]);

