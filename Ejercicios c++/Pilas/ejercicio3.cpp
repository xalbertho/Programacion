#include <iostream>
#include <stdlib.h>

using namespace std;

struct Nodo
{
    int dato;
    Nodo *siguiente;
};

void agregar(Nodo *&, int);
void imprimir(Nodo *&);

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
    
   imprimir(pila);

 
}

void agregar(Nodo *&pila, int n)
{
    Nodo *nuevo_nodo=new Nodo();
    nuevo_nodo->dato=n;
    nuevo_nodo->siguiente=pila;
    pila=nuevo_nodo;

    cout<<"El elemento "<<n<<" Fue agregado correctamente";
}

void imprimir(Nodo *&pila)
{
    cout<<"Eleentos de la pila";
    while(pila!=NULL)
    {
        cout<<pila->dato<< " ,";
        pila=pila->siguiente;
    }
}