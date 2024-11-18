/**
 * @file agenda.cpp
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief
 * @version 0.1
 * @date 2024-03-26
 *
 * @copyright Copyright (c) 2024
 *
 */
#include "agenda.hpp"

using namespace agenda;

// Getters
string Contacto::getNombre() { return this->nombre; }
string Contacto::getApodo() { return this->apodo; }
string Contacto::getNumero() { return this->numero; }

// setters
void Contacto::setNombre(string nombre) { this->nombre = nombre; }
void Contacto::setApodo(string apodo) { this->apodo = apodo; }
void Contacto::setNumero(string numero) { this->numero = numero; }

void Agenda::agregarContacto(string nombre, string apodo, string numero)
{
    lista.emplace_back(nombre, apodo, numero);
    // lista.push_back(Contacto(nombre, apodo, numero));
}

int Agenda::buscarPorNombre(string nombre)
{
    for (int i = 0; i < lista.size(); i++)
    {
        if (lista[i].getNombre() == nombre)
        {
            return i;
        }
    }
    return -1;
}

int Agenda::buscarPorApodo(string apodo)
{
    for (int i = 0; i < lista.size(); i++)
    {
        if (lista[i].getApodo() == apodo)
        {
            return i;
        }
    }
    return -1;
}

void Agenda::actualizar(int idx, string nombre, string apodo, string numero)
{
    if (idx >= 0 && idx < lista.size())
    {
        lista[idx].setNombre(nombre);
        lista[idx].setApodo(apodo);
        lista[idx].setNumero(numero);
    }
}

string Agenda::listar()
{
    string cadena = "";
    for (int i = 0; i < lista.size(); i++)
    {
        cadena += lista[i].getNombre() + " - " + lista[i].getApodo() +
                  " - " + lista[i].getNumero() + "\n";
    }
    return cadena;
}

string Agenda::llamar(int id)
{
    if (id >= 0 && id < lista.size())
    {
        return "Marcando a " + lista[id].getNombre() + " (" + lista[id].getNumero() + ")...";
    }
    else
    {
        return "Error en la llamada...";
    }
}