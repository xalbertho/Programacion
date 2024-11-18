#include <iostream>
using namespace std;


class Cuenta;

class Cliente {
private:
    int numercte;
    Cuenta *cuenta; 
public:
    Cliente() : numercte(0), cuenta(nullptr) {} 
    Cliente(int num) : numercte(num), cuenta(nullptr) {} 
    void AgregarCuenta(Cuenta *c); 
    void Muestra();
};

class Cuenta {
private:
    int numero;
    Cliente cliente; 
public:
    Cuenta() : numero(0) {} 
    Cuenta(int num, int numCliente); 
    void Muestra();
};



void Cliente::AgregarCuenta(Cuenta *c) {
    cuenta = c;
}

void Cliente::Muestra() {
    cout << "Numero de Cliente: " << numercte << endl;
    
    if (cuenta) {
        cuenta->Muestra();
    }
}

Cuenta::Cuenta(int num, int numCliente) : numero(num), cliente(numCliente) {
  
    cliente.AgregarCuenta(this);
}

void Cuenta::Muestra() {
    cout << "Numero de cuenta: " << numero << endl;
    cliente.Muestra();
}

// 