/**
 * @file main.cpp
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief
 * @version 0.1
 * @date 2024-04-29
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <iostream>

using namespace std;

class Fecha
{
private:
    unsigned char _dia;
    unsigned char _mes;
    unsigned short _anio;

public:
    Fecha(int dia, int mes, int anio)
    {
        if (dia <= 0 || dia > 31)
        {
            throw "Dia no valido.";
        }
        if (mes <= 0 || mes > 12)
        {
            throw "Mes no valido.";
        }

        if (anio <= 0 || anio >= 65536)
        {
            throw "Año no valido.";
        }

        this->_dia = dia;
        this->_anio = anio;
        this->_mes = mes;
    }

    int dia() { return this->_dia; }
    int mes() { return this->_mes; }
    int anio() { return this->_anio; }

    void dia(int dia)
    {
        if (dia <= 0 || dia > 31)
        {
            throw "Dia no valido.";
        }
        this->_dia = dia;
    }
    void mes(int mes)
    {
        if (mes <= 0 || mes > 12)
        {
            throw "Mes no valido.";
        }
        this->_mes = mes;
    }

    void anio(int anio)
    {
        if (anio <= 0 || anio >= 65536)
        {
            throw "Año no valido.";
        }
        this->_anio = anio;
    }
};

class Persona
{
protected:
    string _nombre;
    string _curp;
    string _rfc;
    Fecha *_fnacimiento;

    public:

    Persona() {
        _fnacimiento = NULL;
    }

    ~Persona() {
        if(this->_fnacimiento != NULL) {
            delete this->_fnacimiento;
        }
    }
    
    void nombre(string nombre) {
        this->_nombre = nombre;
    }
    void curp(string curp) {
        this->_curp = curp;
    }
    void rfc(string rfc) {
        this->_rfc = rfc;
    }

    void fnacimiento(Fecha f) {
        if(this->_fnacimiento == NULL) {
            this->_fnacimiento = new Fecha(1,1,1);
        }
        this->_fnacimiento->dia(f.dia());
        this->_fnacimiento->mes(f.mes());
        this->_fnacimiento->anio(f.anio());
    }
    void fnacimiento(int dia, int mes, int anio) {
        if(this->_fnacimiento == NULL) {
            this->_fnacimiento = new Fecha(1,1,1);
        }
        this->_fnacimiento->dia(dia);
        this->_fnacimiento->mes(mes);
        this->_fnacimiento->anio(anio);
    }

    string nombre() {return this->_nombre;}
    string curp() {return this->_curp;}
    string rfc() {return this->_rfc;}
    Fecha* fnacimiento() {return this->_fnacimiento;}

};

class Profesor : Persona {
    private:
    int noEmpleado;
    public:

    int num_Empleado() {return this->noEmpleado;}
    void num_Empleado(int numero) { this->noEmpleado = numero; }
    
 };

int main()
{
    Profesor *p = new Profesor();

    delete p;
    
    return 0;
}
