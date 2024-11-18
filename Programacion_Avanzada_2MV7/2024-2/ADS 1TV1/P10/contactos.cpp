/**
 * @file contactos.cpp
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief
 * @version 0.1
 * @date 2024-03-22
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <iostream>
#include"tools.hpp"

using namespace std;

class Contacto
{
private:
    string nombre;
    string apodo;
    string numero;
    int variableInstancia;

public:
    // Constructor
    Contacto(string nombre, string apodo, string numero) {
        this->nombre = nombre;
        this->apodo = apodo;
        this->numero = numero;
    }

    Contacto(string nombre, string numero): 
    nombre(nombre), numero(numero) {
        this->apodo = "Sin apodo";
    } 

    // Destructor
    ~Contacto() {

    }

    // setters
    void setNombre(string nuevo_nombre)
    {
        nombre = nuevo_nombre;
    }

    void setApodo(string apodo)
    {
        this->apodo = apodo;
    }
    void setNumero(string numero)
    {
        this->numero = numero;
    }

    // getters
    string getNombre()
    {
        return nombre;
    }
    string getApodo()
    {
        return this->apodo;
    }
    string getNumero() { return this->numero; }

    void funcion()
    {
        int variableLocal;

        {
            int varibaleBloque;
        }
    }

    void llamar(Contacto c)
    {
        cout << "Llamando a " << c.apodo << "..." << endl;
    }
};

int main()
{

    Contacto contacto1("Alex", "El mecatronico destroza hogares", "666");
    Contacto contacto2("Vanessa", "La bandida", "777");
    Contacto contacto3("Jesus", "567");

    string opciones[] = {"Agregar contacto", "Ver contactos", "Buscar contacto", "Salir"};
    int sel = showMenu(4, opciones, "Agenda de Contactos");

    cout << sel;
    pausa();

   
    
    //contacto1.llamar(contacto3);

    return 0;
}
