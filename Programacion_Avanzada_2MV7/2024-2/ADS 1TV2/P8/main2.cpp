/**
 * @file main.cpp
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief
 * @version 0.1
 * @date 2024-03-22
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <iostream>
#include "tools.hpp"

using namespace std;

class Contacto
{
private:
    string nombre;
    string numero;
    string apodo;
    int variableInstancia;

public:

    // Constructor
    Contacto(string nombre, string apodo, string numero) {
        this->nombre = nombre;
        this->apodo = apodo;
        this->numero = numero;
    }

    Contacto(string nombre, string numero): nombre(nombre), numero(numero) {
        this->apodo = "Sin apodo";
    }

    // Destructor
    ~Contacto() {
        cout << "Me mori";
    }

    // Setters
    void setApodo(string apodo){
        this->apodo = apodo;
    }
    void setNombre(string nuevo_nombre){
        nombre = nuevo_nombre;
    }

    void setNumero(string numero) {
        this->numero = numero;
    }

    // Getters
    string getNombre() {
        return nombre;
    }
    string getNumero() {
        return this->numero;
    }
    string getApodo() {
        return this->apodo;
    }

    // Declararion de funcion
    void funcion();

    void llamar(Contacto c)
    {
        cout << "Llamando a " << c.nombre << endl;
    }
};

// Definicion de funcion
void Contacto::funcion() {
    int variable;
}

int main()
{
    string opciones[] = {"Agregar contacto", "Llamar contacto", "Editar contacto", "Buscar contacto", "Salir"};
    int seleccion = showMenu(5, opciones, "Lista de contactos");

    cout << seleccion;
    return 0;

    Contacto contacto("Camilo", "Garmilos", "777"), contacto2("Leonardo", "Donatelo", "1234");
    Contacto c("Julio", "123");
    //Contacto lista_de_contactos[2];
    //lista_de_contactos[0].llamar(lista_de_contactos[1]);
    
    return 0;
}
