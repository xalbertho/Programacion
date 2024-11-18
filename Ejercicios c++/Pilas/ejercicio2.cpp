/*Hacer un programa para agregar numeros enteros a una
pila, hasta que el usuario lo decida, despues mostrar 
los numeros introduciodos en la pila*/

#include <iostream>
#include <stdlib.h>

using namespace std;

struct Nodo
{
    int dato;
    Nodo *siguiente;
};

void agregar(Nodo *&, int);
void sacar(Nodo *&,int &);
int main(void)
{
    Nodo *pila=NULL;
    int dato;
    char respuesta;
    do
    {
        cout<<"Digite un numero: ";
        cin>>dato;
        agregar(pila, dato);
        cout<<"\nDeseas agregar otro elemento a la pila? (s/n)";
        cin>>respuesta;
    } while (respuesta=='s'||respuesta=='S');
    
    cout<<"Sacando los elementos de la pila: ";

    while(pila!=NULL)
    {
        sacar(pila,dato);
        
        cout<<dato<<" ,";
    }
    cout<<".";


}

void agregar(Nodo *&pila, int n)
{
    Nodo *nuevo_nodo=new Nodo();
    nuevo_nodo->dato=n;
    nuevo_nodo->siguiente=pila;
    pila=nuevo_nodo;

    cout<<"El elemento "<<n<<" Fue agregado correctamente";
}

void sacar(Nodo *&pila, int &n)
{
     Nodo *aux=pila;
     n=aux->dato;
     pila=aux->siguiente;
     delete aux;
}