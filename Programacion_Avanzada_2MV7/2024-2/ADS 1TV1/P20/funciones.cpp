#include "funciones.hpp"

Fecha::Fecha(int dia, int mes, int anio)
{
    if (dia <= 0 || dia > 31)
    {
        throw "Dia invalido.";
    }
    if (mes <= 0 || mes > 12)
    {
        throw "Mes invalido.";
    }
    if (anio <= 0 || anio >= 65536)
    {
        throw "Anio invalido.";
    }
    this->_anio = anio;
    this->_mes = mes;
    this->_dia = dia;
}

void Fecha::dia(int dia)
{
    if (dia <= 0 || dia > 31)
    {
        throw "Dia invalido.";
    }
    this->_dia = dia;
}
int Fecha::dia() { return this->_dia; }

void Fecha::mes(int mes)
{
    if (mes <= 0 || mes > 12)
    {
        throw "Mes invalido.";
    }
    this->_mes = mes;
}

int Fecha::mes() { return this->_mes; }

void Fecha::anio(int anio)
{
    if (anio <= 0 || anio >= 65536)
    {
        throw "Anio invalido.";
    }
    this->_anio = anio;
}
int Fecha::anio() { return this->_anio; }
