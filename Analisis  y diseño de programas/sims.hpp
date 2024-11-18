#include <iostream>
#include <string>

using namespace std;

class Bateria {
private:
    int mAh;
    string marca;
public:
    Bateria(int, string);
    Bateria() {}
    void Muestra();
};
Bateria::Bateria(int a, string b) {
    mAh = a;
    marca = b;
}

void Bateria::Muestra() {
    cout << "Bateria de: " << mAh << " mA" << endl;
    cout << "Marca: " << marca << endl;
}

class Sim {
private:
    string fabricante;
    int num_sim;
public:
    Sim(string, int);
    Sim() {}
    void muestra();
};

Sim::Sim(string a, int b) {
    fabricante = a;
    num_sim = b;
}

void Sim::muestra() {
    cout << "Empresa: " << fabricante << endl;
    cout << "Numero de sim: " << num_sim << endl;
}

class Celular {
private:
    string modelo;
    string marca;
    int cantidad = 0;
    Bateria bateria; // Declaración de Bateria
    Sim chip[2];
public:
    Celular(string, string, int, string);
    void Agregar(Sim);
    void muestra();
};

Celular::Celular(string a, string b, int c, string d) {
    modelo = b;
    marca = a;
    cantidad = 0;
    Bateria x(c, d);
    bateria = x;
}

void Celular::Agregar(Sim a) {
    if (cantidad < 2) {
        chip[cantidad] = a;
        cantidad++;
    }
}

void Celular::muestra() {
    cout << "Marca: " << marca << endl;
    cout << "Modelo: " << modelo << endl;
    cout << "Cantidad: " << cantidad << endl;
    bateria.Muestra();
    for (int i = 0; i < cantidad; i++) {
        chip[i].muestra();
    }
}

