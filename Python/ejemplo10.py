
#sentencias de control en un bucle
#  break, continue, pass 
# continue es mayormente usada en ciclos, donde, esta es ejecutada pasa a la siguiente iteracion en el bucle
#pass es usada donde no se requiere hacer ningua iteraccion con el flujo

while True:
    name=input("Ingrese su nombre: ");
    if name!="":
        break;                          #termina el programa si la condicion es true    

phone_number="124-23-4223-232";

for i in phone_number:
    if i=='-':
        continue;
    print(i,end="");

for i in range(20,35):
    if i==24:
        pass;
    else:
        print(i);
