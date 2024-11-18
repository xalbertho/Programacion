
#include "ejemplo1.hpp"

Complejo operator +(Complejo,Complejo);
int main(void)
{
    int a,b;
    cout<<"Ingresa la parte real:\n";
    cin>>a;
    cout<<"Ingrese la parte imaginaria:\n";
    cin>>b;
    Complejo d(a,b);
    Complejo e;
    Complejo c(a,b);
    e=c+d;
    e.mostrar();
}

Complejo operator +(Complejo x, Complejo y)
{
    Complejo resultado;
    resultado.real=x.real+y.real;
    resultado.imaginario=x.imaginario+y.imaginario;
    return resultado;
}