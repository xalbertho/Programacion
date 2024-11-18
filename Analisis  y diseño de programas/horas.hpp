#include <iostream>

using namespace std;

class Hora {
private:
    int horas;
    int minutos;
    int segundos;

public:
    Hora(); 
    Hora(int h, int m, int s); 
    Hora sumarHoras(Hora h2);
    void imprimir();      
};

Hora::Hora()
{
    cout << "Ingrese la hora: ";
    cin >> horas;
    cout << "Ingrese los minutos: ";
    cin >> minutos;
    cout << "Ingrese los segundos: ";
    cin >> segundos;
}

Hora::Hora(int h, int m, int s)
{
    horas = h;
    minutos = m;
    segundos = s;
}

Hora Hora::sumarHoras(Hora h2)
{
    Hora suma;
    suma.segundos = segundos + h2.segundos;
    suma.minutos = minutos + h2.minutos;
    suma.horas = horas + h2.horas;

    if (suma.segundos >= 60) {
        suma.segundos -= 60;
        suma.minutos++;
    }

    if (suma.minutos >= 60) {
        suma.minutos -= 60;
        suma.horas++;
    }

    return suma;
}

void Hora::imprimir()
{
    cout << horas << ":" << minutos << ":" << segundos << ", hrs.\n";
}
