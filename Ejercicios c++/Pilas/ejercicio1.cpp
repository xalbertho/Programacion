/* Insertar elementos en una pila*/
/* 1.- Crear espacion en memoria
2.- cargar valor dentro del nodo
3.- cargar puntero pila dentro del nodo
4.- asignar el nuevo nodo a pila
usando ptr=null (puntero vacio)*/

#include <iostream>
#include <stdlib.h>

using namespace std;
struct Nodo
{
    int dato;
    Nodo *siguiente;
};

void agregar(Nodo *&,int);
void quitar(Nodo *&, int &);

int main(void)
{
    Nodo *pila=NULL;
    int dato;

    cout<<"Digite un numero: ";
    cin>>dato;
    agregar(pila,dato);

    cout<<"Digite otro  numero: ";
    cin>>dato;
    agregar(pila,dato);

    cout<<"\nSacando los elementos de la pila: ";

    while(pila!=NULL)
    {
        quitar(pila,dato);
       
            cout<<dato<<" ,";
    }
    cout<<".";
}

void agregar(Nodo *&pila,int n)
{
    Nodo *nuevo_nodo=new Nodo();
    nuevo_nodo->dato=n;
    nuevo_nodo->siguiente=pila;
    pila=nuevo_nodo;

     cout<<"\nElemento "<<n<<" agregado a PILA correctamente"<<endl;
}

void quitar(Nodo *&pila, int &n)
{
    Nodo *aux=pila; //Aclarando que  pila tiene el ultimo nodo
    n=aux->dato; // sea n=*n por la declaracion, por lo que almacenara el valor de n
    pila=aux->siguiente; //recordando que una pila va apuntando hacia abajo, por lo que ahora pila tendra el nodo anterior
    delete aux;
}