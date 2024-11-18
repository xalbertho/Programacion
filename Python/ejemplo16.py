# programa para  crear una calculadora con funciones

def suma(x,y):

    return x+y;
def multiplicacion(x,y):
    return x*y
def  positivo(x,y):
    if x >0 & y >0:
        return True;
    elif x<0 and y<0:
        return True;
    else:
        return False;



x=int(input("Ingrese un numero: "));
y=int(input("Ingrese un numero: "));
print("La suma de los numeros",x,"+",y,"es",suma(x,y));
print("La multiplicacion de los numeros",x,"+",y,"es",multiplicacion(x,y));

if positivo==True:
    print("El numero es positivo");

print("el numero es negativo");
