/**
 * @file main3.cpp
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief
 * @version 0.1
 * @date 2024-03-25
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <iostream>
#include <ostream>
#include "tools.hpp"

using namespace std;

class Punto
{
private:
    float x, y;

public:
    Punto(float x = 0.0f, float y = 0.0f) : x(x), y(y) {}

    // getters
    float getX() { return this->x; }
    float getY() { return this->y; }

    // setters
    void setX(float x) { this->x = x; }
    void setY(float y) { this->y = y; }

    // Metodos
    friend Punto operator+(const Punto &p1, const Punto &p2)
    {
        return Punto(p1.x + p2.x, p1.y + p2.y);
    }

    friend ostream& operator <<(ostream &os, const Punto& p) {
        os << "(" << p.x << ", " << p.y << ")";
        return os;
    }
};

int main()
{
    int a = 6, b = 7;
    int c = a + b;
    Punto p1(1, 1), p2(2, 2), p3;
    p3 = p1 + p2;

    cout << p3;

    return 0;
}
