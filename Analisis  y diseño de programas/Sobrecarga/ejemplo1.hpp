#include <iostream>
using namespace std;
class Complejo
{
private:
    int real;
    int imaginario;
public:
    Complejo(int, int);
    Complejo();
    void mostrar();
    friend Complejo operator +(Complejo,Complejo);
};

Complejo::Complejo(int a, int b)
{
    real=a;
    imaginario=b;

}

Complejo::Complejo()
{
    real=0;
    imaginario=0;

}
void Complejo::mostrar()
{
    cout<<real<<" + "<<imaginario<<"i";

}