#include <iostream>
#include <string>

class clase_persona
{
    protected:
    int edad;
    string nombre;

    public:
    clase_persona(string , int);
    clase_persona();
    void muestra_datos();
};

clase_persona::clase_persona()
{
}

clase_persona::~clase_persona()
{
}
