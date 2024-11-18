print("Hello world");
#Algunas tipo de asignaciones de variables

x="Alberto";
y=20;
z=True;

print(x,y,z); #imprime en pantalla solamente
print(type(z)); # imprime el tipo de valor, en este caso z(bool)
print("Hello "+x) #imprime hello mas el valor de la variable x;
y+=1;
print(y);
print(str(y));

height=1.70;
print(type(height));
print("Tu estatura es: "+str(height)); # en python no se pueden concatenar datos, po rlo que es necesario convertir todo a un mismo tipo de dato, en este caso a string

a=b=c=b=12;
print(c);

nombre,edad,atractive="Alberto",21,True; # en python es psoble asignar variables de esta forma
print("Tu nombre es: "+nombre+"tienes: "+str(edad)+" tu eres atractivo?: "+str(atractive));

