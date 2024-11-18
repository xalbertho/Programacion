#funciones= un bloque de codigo que ejecuta una sola tarea

def hello(name,age):
    if name[0].islower:
        name=name.capitalize();
    print("hello",name,"tu tienes",age,"años");
    print("Have a nice day");

name=input("Ingrese tu nombre: ");
age=input("ingresa tu edad: ");
hello(name,age);
