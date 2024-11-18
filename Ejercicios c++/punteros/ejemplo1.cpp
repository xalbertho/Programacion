/* comprueba si un numero es par 
o impar, señala la posicion de memoria
usa punteros*/

#include <iostream>

using namespace std;

int main(void){


    int numero, *dir_num;
    dir_num=&numero;
    cout<<"Ingrese el numero";
    cin>>numero;

    (*dir_num%2==0) ? cout<<"El numero es par" : cout<<"El numero es impar";
    cout<<dir_num; 

}