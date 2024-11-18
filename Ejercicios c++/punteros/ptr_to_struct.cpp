/* ahora analizemos los punteros a las estructuras*/
#include <iostream>
#include <conio.h>

using namespace std;

struct Persona
{
    char nombre[30];
    int edad;
} persona, *puntero_persona=&persona;


void pedir(void);
void mostrar(Persona *);

int main(void)
{
pedir();
mostrar(puntero_persona);

}
void pedir(void)
{
    cout<<"Ingrese su nombre: "; 
    cin.getline(puntero_persona->nombre,30,'\n');
    cout<<"Ingrese su edad: ";
    cin>>puntero_persona->edad;
}

void mostrar(Persona *puntero_persona)
{
    cout<<"Nombre: "<<puntero_persona->nombre<<endl;
    cout<<"edad"<<puntero_persona->edad;
}