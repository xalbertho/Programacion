
# <<<<<------STRING METHODS------->>>>
name="Alberto";

print(name.find("o")); #encuentra la posicion del caracter, empezando de cero
print(len(name));#longitud de la cadena, empieza en 1
print(name.capitalize()); #hace la primera letra del string en mayuscula
print(name.upper());#convierte el string a mayusculas
print(name.lower());#convierte el string a minusculas
print(name.isdigit());# metodo tipo bool, devuelve true si todos los elementos de la cadena son numeros, false si no lo son
print(name.isalpha());# metodo para verificar si todos los elementos del string son del alfabeto(mayusculas o minusculas) tipo bool;
print(name.count("o"));# metodo para contar cuantas veces en un string se repite un substring o caracter
print(name.replace("o","a")); #metodo para remplazar caracteres
print(name*3);# imprime 3 veces name

 
