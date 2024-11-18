/*Bloque de ounteros
Rellenar un arreglo con n numeros, posteriormente utilizando punteros
determina el menor elemento del arreglo*/

#include <iostream>
using namespace std;
int main(void){
    int numeros[5];
    int *dir;
    dir=numeros;
    int numero_menor=*dir;

    for(int i=0;i<5;i++)
    {
        cout<<"Ingresa ele elemento[ "<<i<<"]"<<endl;
         cin>>numeros[i];
         
    }

    for(int i=0;i<5;i++)
    {
        if(*dir<numero_menor)
        {
            numero_menor=*dir;
        }
        *dir++;
    }
    cout<<numero_menor;


}