#include <iostream>

class Rectangulo {
private:
    double longitud;
    double ancho;

public:
    Rectangulo(double l, double w) : longitud(l), ancho(w) {}

    double calcularArea() {
        return longitud * ancho;
    }
};
