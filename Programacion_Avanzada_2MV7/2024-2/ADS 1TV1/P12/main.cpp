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
#include <iostream>
#include <vector>
#include "agenda.hpp"
#include "tools.hpp"

using namespace std;
using namespace agenda;

int main()
{
    Agenda agenda;
    char nombre[200], apodo[100], telefono[20];

    int sel = 0;
    string opciones[] = {"Agregar contacto", "Llamar contacto", "Editar contacto", "Listar", "Salir"};
    string opciones2[] = {"Buscar por nombre", "Buscar por apodo", "Regresar"};
    do
    {
        sel = showMenu(5, opciones, "Agenda de Contactos");

        switch (sel)
        {
        case 0:
            cout << "Escriba el nombre: ";
            cin.getline(nombre, 200);
            cout << "Escriba el apodo: ";
            cin.getline(apodo, 100);
            cout << "Escriba el telefono: ";
            cin.getline(telefono, 20);
            agenda.agregar(nombre, apodo, telefono);
            break;
        case 1:
            sel = showMenu(3, opciones2, "Llamar a un contacto");
            switch (sel)
            {
            case 0:
                cout << "Ingrese el nombre: ";
                cin.getline(nombre, 200);
                sel = agenda.buscarPorNombre(nombre);
                cout << agenda.llamar(sel);
                sel = 0;
                pausa();
                break;
            case 1:
                cout << "Ingrese el apodo: ";
                cin.getline(apodo, 100);
                sel = agenda.buscarPorApodo(apodo);
                cout << agenda.llamar(sel);
                sel = 0;
                pausa();
                break;
            default:
                break;
            }
            break;
        case 2:
            sel = showMenu(3, opciones2, "Editar a un contacto");
            if (sel == 2)
            {
                sel = 0;
                break;
            }
            switch (sel)
            {
            case 0:
                cout << "Ingrese el nombre: ";
                cin.getline(nombre, 200);
                sel = agenda.buscarPorNombre(nombre);

                break;
            case 1:
                cout << "Ingrese el apodo: ";
                cin.getline(apodo, 100);
                sel = agenda.buscarPorApodo(apodo);
                break;
            default:
                break;
            }

            if (sel == -1)
            {
                cout << "El contacto no existe.";
                pausa();
                sel = 0;
                break;
            }
            else
            {
                cout << "Escriba el nombre: ";
                cin.getline(nombre, 200);
                cout << "Escriba el apodo: ";
                cin.getline(apodo, 100);
                cout << "Escriba el telefono: ";
                cin.getline(telefono, 20);
                agenda.actualizar(sel, nombre, apodo, telefono);
                sel = 0;
            }
            break;
        case 3:
            cout << agenda.listar();
            pausa();
            break;
        default:
            break;
        }
    } while (sel != 4);

    return 0;
}
