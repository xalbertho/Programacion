/**
 * @file puntos.cpp
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief
 * @version 0.1
 * @date 2024-03-25
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <iostream>

using namespace std;

class Punto
{
private:
    float x, y;

public:
    Punto(float x, float y) : x(x), y(y) {}

    // getters
    float getX() { return this->x; }
    float getY() { return this->y; }

    // setters
    void setX(float x) { this->x = x; }
    void setY(float y) { this->y = y; }

    // Metodo
    friend Punto operator+(const Punto &p1, const Punto &p2)
    {
        return Punto(p1.x + p2.x, p1.y + p2.y);
    }

    friend ostream& operator <<(ostream &os, const Punto &p) {
        os << "(" << p.x << ", " << p.y << ")";
        return os;
    }
};

int suma(int a, int b)
{
    a = 10;
    b = 3;
    return a + b;
}
int sumaRef(int *a, int *b)
{
    *a = 10;
    *b = 3;
    return *a + *b;
}

int sumaRefCpp(int &a, int &b)
{
    a = 10;
    b = 3;
    return a + b;
}

int main()
{
    int x = 5, y = 6;
    cout << sumaRefCpp(x, y) << endl;
    //cout << x << "," << y;

    //return 0;

    Punto p1(1, 1), p2(1, 3);
    p1.getX();

    Punto p3 = p1 + p2;

    //cout << p3.getX() << ", "<< p3.getY();
    cout << p3;

    return 0;
}
