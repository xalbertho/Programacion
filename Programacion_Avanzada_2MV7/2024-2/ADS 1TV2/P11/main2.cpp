/**
 * @file main2.cpp
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief
 * @version 0.1
 * @date 2024-04-12
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <iostream>

using namespace std;

class Alumno
{
private:
    string nombre;
    string boleta;

public:
    Alumno(string nombre, string boleta) : nombre(nombre), boleta(boleta) {}

    // getters
    string getNombre() { return this->nombre; }
    string getBoleta() { return this->boleta; }

    // setters
    void setNombre(string nombre) { this->nombre = nombre; }
    void setBoleta(string boleta) { this->boleta = boleta; }
};

int main()
{
    Alumno *a1;
    Alumno a2("Camilo", "20202030");
    a1 = new Alumno("Pedro", "20202020");

    cout << a1->getNombre() << endl;
    cout << a2.getNombre();

    delete a1;

    return 0;
}
