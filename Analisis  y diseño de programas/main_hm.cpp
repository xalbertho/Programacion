
#include "herencia_multiple.hpp"


int main()
{
    string des,tipoh;
    int asi,dias;
    cout<<"Ingrese el destino a viajar: ";
    cin>>des;
    cout<<"Ingrese el numero de dias: ";
    cin>>dias;
    cout<<"Elige el numero de asiento(1-20): ";
    cin>>asi;
    cout<<"Ingrese el tipo de habitacion: ";
    cin>>tipoh;
    PlanV viaje(des,dias,asi,tipoh);
    viaje.imprimeCosto();
}