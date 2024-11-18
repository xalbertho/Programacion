#include <iostream>
using namespace std;

class Elemento {
private:
    float peso_molecular;
    float num_moleculas;
    int num_atomos;
    float peso_total;

public:
    void pedirDatos();
    void calcularPesoTotal();
    void mostrarPesoTotal();
};

void Elemento::pedirDatos() {
    cout << "Ingrese la masa atómica del elemento: ";
    cin >> peso_molecular;
    cout << "Ingrese el número de moléculas que contiene: ";
    cin >> num_moleculas;
    cout << "Ingrese el número de átomos del elemento: ";
    cin >> num_atomos;
}

void Elemento::calcularPesoTotal() {
    peso_total = peso_molecular * num_atomos * num_moleculas;
}

void Elemento::mostrarPesoTotal() {
    cout << "El peso molecular total es: " << peso_total << endl;
}