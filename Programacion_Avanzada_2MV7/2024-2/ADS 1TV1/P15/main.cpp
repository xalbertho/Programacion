/**
 * @file main.cpp
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

class Alumno {
    private:
    string nombre;
    string boleta;

    public:
    Alumno(string nombre, string boleta) : nombre(nombre), boleta(boleta) {}

    // getters
    string getNombre() {return this->nombre;}
    string getBoleta() {return this->boleta;}

    // setters
    void setNombre(string nombre) {this->nombre = nombre;}
    void setBoleta(string boleta) {this->boleta = boleta;}

};

void nada()
{
    Alumno *al1 = new Alumno("Alex", "2009");
    Alumno al2("Axel", "2024");

    cout << al2.getNombre() ;
    cout << al1->getNombre();


    int **arr;
    arr = new int*[2];
    *(arr+0) = new int[2];
    *(arr+1) = new int[2];
    
    
    delete[] arr[0];
    delete[] arr[1];
    delete[] arr;
    
}

int main()
{
    while (true)
    {
        nada();
    }
    
    
    return 0;
}
