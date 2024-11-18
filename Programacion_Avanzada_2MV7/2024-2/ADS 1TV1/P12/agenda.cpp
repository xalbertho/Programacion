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
#include <iostream>
#include "agenda.hpp"

using namespace std;
using namespace agenda;

// getters
string Contacto::getNombre() { return this->nombre; }
string Contacto::getApodo() { return this->apodo; }
string Contacto::getNumero() { return this->numero; }

// setters
void Contacto::setNombre(string nombre) { this->nombre = nombre; }
void Contacto::setApodo(string apodo) { this->apodo = apodo; }
void Contacto::setNumero(string numero) { this->numero = numero; }

void Agenda::agregar(string nombre, string apodo, string numero)
{
    lista.emplace_back(nombre, apodo, numero);
    // lista.push_back(Contacto(nombre, apodo, numero));
}

int Agenda::buscarPorNombre(string nombre)
{
    for (int i = 0; i < lista.size(); i++)
    {
        if (lista[i].getNombre() == nombre)
            return i;
    }
    return -1;
}

int Agenda::buscarPorApodo(string apodo)
{
    for (int i = 0; i < lista.size(); i++)
    {
        if (lista[i].getApodo() == apodo)
            return i;
    }
    return -1;
}

void Agenda::actualizar(int id, string nombre, string apodo, string numero)
{
    if (id >= 0 && id < lista.size())
    {
        lista[id].setNombre(nombre);
        lista[id].setApodo(apodo);
        lista[id].setNumero(numero);
    }
}

string Agenda::listar()
{
    string str = "";
    for (int i = 0; i < lista.size(); i++)
    {
        str += lista[i].getNombre() + " - " + lista[i].getApodo() + " - " + lista[i].getNumero() + "\n";
    }
    return str;
}

string Agenda::llamar(int idx)
{
    if (idx >= 0 && idx < lista.size())
    {
        return "Llamando a " + lista[idx].getNombre() + " (" + lista[idx].getNumero() + ")...";
    }
    else
    {
        return "Error en la llamada...";
    }
}