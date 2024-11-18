#include <iostream>
#include <string>
using namespace std;

class Resistencia {
protected:
    int valor;
    string tipoDeMedida;
    float costoR;

public:
    Resistencia(int val, const string& tipo, float costo);
    void Muestra() const;
};

class Compuertas {
protected:
    string tipo;
    float costoC;

public:
    Compuertas(const string& t, float costo);
    void Mostrar() const;
};

class LED {
protected:
    string color;
    float costoL;

public:
    LED(const string& c, float costo);
    void MuestraDatosL() const;
};

class Circuito : public Resistencia, public Compuertas, public LED {
protected:
    string nombre;
    string colorProto;

public:
    Circuito(const string& n, const string& c, int valRes, const string& tipoRes, float costoRes, 
             const string& tipoComp, float costoComp, const string& colorLED, float costoLED);
    float CalculaCosto(int numRes, int numComp, int numLed) const;
    void MuestraDatos() const;
};

Resistencia::Resistencia(int val, const string& tipo, float costo) : valor(val), tipoDeMedida(tipo), costoR(costo) {}

void Resistencia::Muestra() const {
    cout << "Resistencia: " << valor << " " << tipoDeMedida << ", Costo: $" << costoR << endl;
}

Compuertas::Compuertas(const string& t, float costo) : tipo(t), costoC(costo) {}

void Compuertas::Mostrar() const {
    cout << "Compuerta: " << tipo << ", Costo: $" << costoC << endl;
}

LED::LED(const string& c, float costo) : color(c), costoL(costo) {}

void LED::MuestraDatosL() const {
    cout << "LED: Color " << color << ", Costo: $" << costoL << endl;
}

Circuito::Circuito(const string& n, const string& c, int valRes, const string& tipoRes, float costoRes, 
                   const string& tipoComp, float costoComp, const string& colorLED, float costoLED)
    : Resistencia(valRes, tipoRes, costoRes), Compuertas(tipoComp, costoComp), LED(colorLED, costoLED), 
      nombre(n), colorProto(c) {}

float Circuito::CalculaCosto(int numRes, int numComp, int numLed) const {
    return numRes * costoR + numComp * costoC + numLed * costoL;
}

void Circuito::MuestraDatos() const {
    cout << "Circuito: " << nombre << ", Color del prototipo: " << colorProto << endl;
    Resistencia::Muestra();
    Compuertas::Mostrar();
    LED::MuestraDatosL();
}