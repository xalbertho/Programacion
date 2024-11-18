#include "horas.hpp"
using namespace std;

int main() {
    Hora h1; 
    Hora h2(12, 45, 30);  

    Hora suma = h1.sumarHoras(h2);

    cout << "La suma de las dos horas es: ";
    suma.imprimir();

    return 0;
}