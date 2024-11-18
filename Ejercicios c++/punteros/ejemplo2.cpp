/* comprueba si es un numero  
primo, señala la posicion de memoria
usa punteros*/

#include <iostream>

using namespace std;

int main(void){


    int numero, *dir_num;
    dir_num=&numero;
    cout<<"Ingrese el numero: ";
    cin>>numero;
    (*dir_num==2)?cout<<"El numero es primo\n" : ((*dir_num%2==0 && *dir_num/ *dir_num==1 && *dir_num/1==*dir_num) ? cout<<"El numero es primo\n" : cout<<"El numero no es primo\n");
    
    cout<<dir_num; 

}