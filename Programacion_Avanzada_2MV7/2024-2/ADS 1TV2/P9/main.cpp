/**
 * @file main.cpp
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief
 * @version 0.1
 * @date 2024-03-26
 *
 * @copyright Copyright (c) 2024
 *
 */

#include "agenda.hpp"
#include "tools.hpp"

using namespace std;
using namespace agenda;

int main()
{
    int sel = 0;
    char nombre[200], apodo[50], telefono[20];
    Agenda miAgenda;
    string opciones[] = {"Agregar contacto", "Llamar contacto", "Actualizar contacto", "Lista Contactos", "Salir"};
    string opciones2[] = {"Buscar por Nombre", "Buscar por Apodo", "Regresar"};

    do
    {
        sel = showMenu(5, opciones, "Agenda de Contactos");

        switch (sel)
        {
        case 0:
            cout << "Ecriba el nombre del contacto: ";
            cin.getline(nombre, 200);
            cout << "Ecriba el apodo del contacto: ";
            cin.getline(apodo, 50);
            cout << "Ecriba el telefono del contacto: ";
            cin.getline(telefono, 20);
            miAgenda.agregarContacto(string(nombre), string(apodo), string(telefono));
            break;
        case 1:
            sel = showMenu(3, opciones2, "Llamar a contacto");
            switch (sel)
            {
            case 0:
                cout << "Escriba el nombre: ";
                cin.getline(nombre, 200);
                sel = miAgenda.buscarPorNombre(string(nombre));
                cout << miAgenda.llamar(sel);
                pausa();
                break;
            case 1:
                cout << "Escriba el apodo: ";
                cin.getline(apodo, 50);
                sel = miAgenda.buscarPorApodo(string(apodo));
                cout << miAgenda.llamar(sel);
                pausa();
                break;
            default:
                break;
            }
            sel = 0;
            break;
        case 2:
            sel = showMenu(3, opciones2, "Actualizar contacto");
            if (sel >= 2)
                break;
            switch (sel)
            {
            case 0:
                cout << "Escriba el nombre: ";
                cin.getline(nombre, 200);
                sel = miAgenda.buscarPorNombre(string(nombre));
                break;
            case 1:
                cout << "Escriba el apodo: ";
                cin.getline(apodo, 50);
                sel = miAgenda.buscarPorApodo(string(apodo));
                break;
            default:
                break;
            }
            if (sel == -1)
            {
                cout << "Contacto no encontrado...";
                pausa();
                break;
            }
            else
            {
                cout << "Ecriba el nombre del contacto: ";
                cin.getline(nombre, 200);
                cout << "Ecriba el apodo del contacto: ";
                cin.getline(apodo, 50);
                cout << "Ecriba el telefono del contacto: ";
                cin.getline(telefono, 20);
                miAgenda.actualizar(sel, nombre, apodo, telefono);
                pausa();
            }
            sel = 0;
            break;
        case 3:
            cout << miAgenda.listar();
            pausa();
            break;
        default:
            break;
        }
    } while (sel != 4);

    return 0;
}
