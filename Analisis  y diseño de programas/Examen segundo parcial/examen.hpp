#include <iostream>
#include <string>
using namespace std;

class Telefonia {
protected:
    string NoTelefono;
    float Mensualidad;

public:
    Telefonia(int noTelefono);
};

class Internet {
protected:
    int Velocidad;
    float Costo;

public:
    Internet(int velocidad);
};

class Cliente : public Telefonia, public Internet {
protected:
    string Nombre;
    string Domicilio;
    int tipocliente;

public:
    Cliente(string nombre, string domicilio, int tipoCliente, int noTelefono, int velocidad);
    float CalculaMes();
    void MuestraDatos();
};


Telefonia::Telefonia(int noTelefono) : Mensualidad(480.0) {
    NoTelefono = to_string(noTelefono);
}


Internet::Internet(int velocidad)
 {
    Velocidad = velocidad;
    if (velocidad <= 10) {
        Costo = 500.0;
    } else if (velocidad <= 50) {
        Costo = 800.0;
    } else {
        Costo = 1200.0;
    }
}

Cliente::Cliente(string nombre, string domicilio, int tipoCliente, int noTelefono, int velocidad)
    : Telefonia(noTelefono), Internet(velocidad), Nombre(nombre), Domicilio(domicilio), tipocliente(tipoCliente) {}

float Cliente::CalculaMes() {
    float total = Mensualidad + Costo;
    if (tipocliente == 0) {
        total *= 0.75; // agregamos el 25% de descuento a los trabajadores
    }
    return total;
}

void Cliente::MuestraDatos() {
    cout << "Nombre: " << Nombre << endl;
    cout << "Domicilio: " << Domicilio << endl;
    cout << "No. Telefono: " << NoTelefono << endl;
    cout << "Velocidad de Internet: " << Velocidad << " Mbps" << endl;
    cout << "Mensualidad de Telefono: $" << Mensualidad << endl;
    cout << "Costo de Internet: $" << Costo << endl;
    cout << "Total a pagar: $" << CalculaMes() << endl;
}