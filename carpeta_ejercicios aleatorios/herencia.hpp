#include <iostream>
#include <string>

using namespace std;

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

clase_persona::clase_persona(string a, int b)
{
    nombre=a;
    edad=b;
}

clase_persona::clase_persona()
{
    cout<<"constructor vacio";
}
void clase_persona::muestra_datos()
{
    cout<<"Hola soy: "<<nombre<<" tengo: "<<edad<<" años";
}


class Estudiante: public clase_persona
{
private:
    int boleta;
    string carrera;
public:
    Estudiante(int, string, int, string);
    void muestra();
};

Estudiante::Estudiante(int a, string b, int c, string d): clase_persona(a, b)

void Estudiante::muestra()
{
    muestra_datos();
    cout<<" Mi boleta es: "<<boleta<<" y estudio: "<<carrera;
}


class Docente: public clase_persona
{
private:
    nom_empleado;
public:
    Docente(int,string,int);
    void muestra();
};

Docente::Docente(int a, string b, int d): clase_persona(a,b), nom_empleado(d)
