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

using namespace std;

class Contacto
{
private:
    string nombre;
    string numero;
    string apodo;
    int variableInstancia;

public:
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

    void funcion()
    {
        int variableLocal;

        {
            int variableBloque;
        }
        
    }

    void llamar(Contacto c)
    {
        cout << "Llamando a " << c.nombre << endl;
    }
};

int main()
{
    Contacto contacto, contacto2;
    
    contacto.setNombre("Camilo");
    contacto.setApodo("Garmilos");
    contacto.setNumero("7777");

    contacto2.setNombre("Leonardo");
    contacto2.setApodo("Donatelo");
    contacto2.setNumero("4798");

    contacto.llamar(contacto2);

    return 0;
}
