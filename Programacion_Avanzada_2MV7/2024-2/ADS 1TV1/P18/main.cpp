/**
 * @file main.cpp
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

class Figura
{
protected:
    double base;
    double altura;

public:
    /**
     * @brief Devuelve el area de la figura
     * 
     * @return double Area de la figura
     */
    virtual double Area()=0;

    virtual double perimetro()=0;
};

class Rectangulo : public Figura
{
    public:
    void fun( ) {
        
    }
};

class Cuadrado : public Figura
{
    public:
    Cuadrado(double lado) {
        this->base= lado;
        this->altura = lado;
    }
    double Area() override
    {
        return base * altura;
    }
    double perimetro() override {
        return 4*base;
    }
};

class Triangulo : public Figura
{
};

int main()
{
    Cuadrado c(6);

    
    
    

    return 0;
}
