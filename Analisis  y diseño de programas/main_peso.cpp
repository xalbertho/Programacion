#include <iostream>
#include "peso.hpp"

using namespace std;

int main() {
    Elemento elemento;
    char respuesta;

    do {
        elemento.pedirDatos();
        elemento.calcularPesoTotal();
        elemento.mostrarPesoTotal();

        cout << "¿Desea agregar otro elemento? (s/n): ";
        cin >> respuesta;
    } while (respuesta == 's' || respuesta == 'S');

    return 0;
}