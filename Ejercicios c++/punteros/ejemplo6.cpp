/* Hcer una funcion para almacenar N numeros en un 
arreglo dinamico, en una funcion independiente
busca un numero en particular, usando cualquier metodo 
de busqueda*/
//trakas hijuesuchingDAMADRE
#include <iostream>

using namespace std;

void pedir(int n, int*);
bool buscar(int n,int num, int *);

int main(void)
{
int n=0,num_buscado=0;

cout<<"Ingrese el numero de elementos: \n";cin>>n;
int numeros[n]={0};
pedir(n,numeros);
cout<<"Ingresa el numero a buscar: "; cin>>num_buscado;
bool comrpobar=buscar(n,num_buscado,numeros);

if(comrpobar){
    cout<<"El elemento esta en el arreglo";
}
else
{
    cout<<"El elemento no esta en el arreglo";
}

}

void pedir(int n, int *numeros)
{
    for(int i=0; i<n;i++)
    { 
        cout<<"Ingrese el elemento ["<<i+1<<"]:\n";
        cin>>*(numeros+i);
    }
}

bool buscar(int n,int num, int *numeros)
{
    for(int i=0; i<n;i++)
    {
        if(*(numeros+i)==num)
        {
            //cout<<"El numero: ["<<*(numeros+i)<<"] esta en el arreglo";
            return true;
        }else{
          continue;
        }
    }
    return false;
}