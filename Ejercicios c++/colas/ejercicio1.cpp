/*----una cola es una estructura de datos caraterizada por ser
una secuencia de elementos en la que la operacion de 
insercion se realiza por un extremo y la extraccion por
el otro----*/
/*---Estructura FIFO (first input, first output)
El primero en entrar es el ´primero en salir----*/

//Insertar elementos en una cola
/*
--1/ crear espacio en memoria
--2/ asignar ese nuevo nado al dato que queremos insertar
--3 Asignar punteros frente y fin*/

#include <iostream>
#include <stdlib.h>

using namespace std;

// creamos una structura llamanda nodo, la cual contiene dos valores un tipo int, y uno tipo Nodo, el cual es un puntero que nos servira para
// apuntar al siguiente nodo, como lo vayamos requiriendo
struct Nodo
{
    int dato;
    Nodo *siguiente;
};

//creamos las funciones, la primera tendra como argumentos 2 Nodos, y el valor a agregar en la pila, se hace el paso por referencia y recordando que son punteros


void insertar_cola(Nodo *&,Nodo *&, int );
bool cola_vacia(Nodo *);

int main(void)
{
    //creamos 2 nodos los cuales apuntaran a NULL, en un principio para no generar problemas y tener la direccion de memoria 
    Nodo *frente=NULL;
    Nodo *fin=NULL;
    
    int dato;
    cout<<"Ingrese un numero";
    cin>>dato;
    insertar_cola(frente,fin,dato);


}

void insertar_cola(Nodo *&frente, Nodo *&fin, int n)
{   
    //creamos una variable de tipo Nodo, llamada nuevo_nodo y reservamos la memoria necesaria
     Nodo *nuevo_nodo=new Nodo();

     //del elemento int de nuevo nodo le asignamos el valor n, que es el elemento que se desea insertar
     nuevo_nodo->dato=n;
     // para  su valor siguiente, lo asignamos como un valor nulo

     nuevo_nodo->siguiente=NULL;

// verifivamos si la cola esta vacia, o ya tiene algun elemento
     if(cola_vacia(frente))
     {
        // en caso de estar vacia, el nodo frente es igual al nuevo nodo
        frente=nuevo_nodo;
     }else
     {
        //caso contrario, del nodo fin, en su valor siguiente, asignamos la direccion del nuevo nodo; para que apunte en esa direccion (primer bit)
        // esto es con el fin de actualizar la direccion en la que apunta fin, ya que si solo actualizamos el nodo fin, este seguira apuntando al primer nodo(frente)
        fin->siguiente=nuevo_nodo;
     }


    // por ultimo asignamos el nnuevo nodo, al nodo fin ---->[nuevo_nodo]
     fin =nuevo_nodo;

}


bool cola_vacia(Nodo *frente)
{
  return (frente==NULL)? true: false;
}