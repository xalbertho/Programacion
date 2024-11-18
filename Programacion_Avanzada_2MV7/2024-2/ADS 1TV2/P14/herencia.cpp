/**
 * @file herencia.cpp
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief
 * @version 0.1
 * @date 2024-04-18
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <iostream>

using namespace std;

class Figura {
    protected:
    double altura;
    double base;
    public:
    virtual double Area()=0;
    virtual double perimetro()=0;
};

class Cuadrado : public Figura
{
    public:
    void fun() {
        
    }
};

class Rectangulo : public Figura
{
    public:
    Rectangulo(double base, double altura)
    {
        this->base = base;
        this->altura= altura;
    }
    // Sobre escritura de metodo
    double Area() {
        return base * altura;
    }
};

class Triangulo : public Figura
{
    public:
    void fun() {
        
    }
};

int main()
{
    Triangulo t;
    Rectangulo r(5,6);
    cout << r.Figura::Area();
    
    
    
    

    return 0;
}
