/*
uso de new, delete*/

#include <iostream>
#include <stdlib.h>
using namespace std;

void pedir_notas():
int num_cal,*calif
int main(void){

}

void pedir_notas(){
    cout<<"Ingrese el numero de calificaciones";
    cin>> num_cal;

    calif=new int[num_cal]; // creamos un arreglo dinamico
    for(int i=0;i<num_cal;i++)
    {
        cout<<"Ingresa una nota"
        cin>>calif[i];

    }
}