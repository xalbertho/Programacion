/*Pedir al usuario N numeros
almacenarlos y despues ordenarlos de forma ascendente
imprimirlos en pantalla usando punteros*/
/*for this case, i use the bobble sort
YA QUE EL TAMAÑP DE elementos a ordenar es muy poco para considerar
usar otro tipo de ordenamierno como el merge sort*/

#include <iostream>
using namespace std;


void pedir_nun(int n, int *arreglo);
void ordenar(int n, int *arreglo);
void imprimir(int n, int *arreglo);


int main(void)
{
    int n=0;
    cout<<"ingrese el numero de elementos: \n"; cin>>n;

    int arreglo[n]={0};
    pedir_nun(n,arreglo);
    ordenar(n,arreglo);
    imprimir(n,arreglo);
}

void pedir_nun(int n, int *arreglo)  

{
    for(int i=0; i<n;i++)
    {
        cout<<"Ingrese el elemento[ "<<i+1<<" ]"<< endl;
        cin>>*arreglo;
        *arreglo++;
    }
}

void ordenar(int n, int *arreglo)
{
    for(int i=0; i<n-1;i++)
    {
        for(int j=0;j<n-1;j++)
        {
            if( *(arreglo + i )>*(arreglo+j+1))
            {
                int aux=*(arreglo+i);
                *(arreglo+i)=*(arreglo+j+1);
                *(arreglo+j+1)=aux;
                
            }
        }
    }
}

void imprimir(int n, int *arreglos)
{
    for(int i=0;i<n;i++){
        cout<< *arreglos<<" ";
        *arreglos++;
    }
}