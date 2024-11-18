#include "electronica.hpp"
#include <iostream>

using namespace std;

int main() {

    Resistencia resistor(100, "ohms", 5.0);
    resistor.Muestra(); 
    Compuertas compuertaAND("AND", 2.0);
    compuertaAND.Mostrar(); 
    LED ledRojo("rojo", 0.50);
    ledRojo.MuestraDatosL(); 

    Circuito circuito("Circuito1", "Rojo", 100, "ohms", 5.0, "AND", 2.0, "rojo", 0.50);
    circuito.MuestraDatos();
 
    float costoTotal = circuito.CalculaCosto(2, 1, 3);
    cout << "El costo total del circuito es: $" << costoTotal << endl;


    
    return 0;
}
