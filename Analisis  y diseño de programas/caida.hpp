#include <iostream>

using namespace std;


class Velocidad
{
    float velocidadi;
    float tiempo;

    public :
    void Capturar();
    float Calcular();
    void Mostrar();

};


void Velocidad::Capturar()
{
    cout<<"Ingrese la velocidada inicial: "<<endl;
    cin>> velocidadi;
    cout<<"Ingrese el tiempo: "<<endl;
    cin>>tiempo;

}

float Velocidad::Calcular()
{
    float g=9.81;
    float vel=velocidadi+g*tiempo;
    return vel;

}

void Velocidad::Mostrar()
{
    cout<<"La velocidad fue: "<<Calcular()<<endl;
}

