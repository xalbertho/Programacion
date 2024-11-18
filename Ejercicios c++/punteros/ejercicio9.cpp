/*Realizar la suma de 2 matrices dinamicas (usando punteros)*/

#include <iostream>
#include <stdlib.h> 

using namespace std;

void pedir();
void asignar_memoria(int **);
/// @brief 
/// @param  
void solicitar(int **);
void calcular_r(void);

int **mat1,**mat2,**resultado,nf,nc;

int main(void)
{
    pedir();

}

void pedir()
{
    cout<<"Ingrese el numero de filas: "; cin>>nf;
    cout<<"Ingrese el numero de columnas: "; cin>>nc;

    mat1=new int *[nf];
    mat2=new int *[nf];
    resultado=new int *[nf];

     for(int i=0; i<nc;i++)
    {
        mat1[i]=new int [nc];
         mat2[i]=new int [nc];
         resultado[i]=new int [nc];
    }
   
  
    solicitar(mat1);
    solicitar(mat2);
    calcular_r();

     for(int i=0; i<nf;i++)
    {
        for(int j=0; j<nc;j++)
        {
            cout<<*(*(resultado)+j);
            cout<<" ";
        }
        cout<<"\n";
    }
    

}

void solicitar(int **mat)
{
    cout<<"Ingrese los elementos de la matriz:\n";
    for(int i=0; i<nf;i++)
    {
        for(int j=0; j<nc;j++)
        {
            cout<<"Ingrese el elemento ["<<i+1<<"]";
            cin>>*(*(mat+i)+j);
        }
    }
}

void calcular_r(void)
{
    for(int i=0;i<nf;i++)
    {
        for(int j=0;j<nc;j++)
        {
           *( *(resultado+i)+j)=(*(*(mat1+i)+j)) + (*(*(mat2+i)+j));
        }
    }
}

