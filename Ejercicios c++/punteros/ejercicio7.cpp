/*
Para este programa se le solicita al usuario una matriz y la guardamos usando punteros
ademas de los comandos new para que la memoria sea dinamica y se almacene a la cantidada
de elementos que el usuario desea ingresar*/
/*Ejercio de punteros para matrices dinamicas
**puntero_matriz -> *puntero_filas [int] [int ] [int]
                    *úntero_fila -> [int] [int]
                    *puntero fika

1 2 3 
4 5 6
7 8 9 */

#include <iostream>
#include <stdlib.h> //new y delete 

using namespace std;

void pedird_datos(void);
void imprimir(int **);

int **puntero_matriz,nfilas,ncolumnas;

int main(void)
{

pedird_datos();
imprimir(puntero_matriz);

}


void pedird_datos(void)
{
    cout<<"Ingrese el numero de filas: ";
    cin>> nfilas;
    cout<<"Ingrese el numero de columnas: ";
    cin>>ncolumnas;
    
    puntero_matriz=new int*[nfilas]; //reservando memoria para las filas


    for(int i=0; i<nfilas;i++)
    {
        puntero_matriz[i]=new int[ncolumnas]; //reservando memoria para las columnas

    }


    cout<<"\nDigite elementos de la matriz\n";
    for(int i=0;i<nfilas;i++)
    {
        for(int j=0;j<ncolumnas;j++)
        {
            cout<<"Digite un numeto["<<i+1<<"] ["<<j+1<<"]";
            cin>>*(*(puntero_matriz+i)+j); //puntero matriz[i][j]
        }
        
    }
}

void imprimir(int **matriz)
{
    cout<<"La matriz ingresada es:\n";

    for(int i=0;i<nfilas;i++)
    {
        for(int j=0; j<ncolumnas; j++)
        {
            cout<<*(*(matriz+i)+j); //puntero_matriz[i][j]
            cout<<" ";
        }
        cout<<"\n";
    }
}