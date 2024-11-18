/**
 * @file main2.cpp
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Menu
 * @version 0.1
 * @date 2024-03-05
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <iostream>

using namespace std;

int main()
{
    int seleccion;

    {
        int a;
        //cout << seleccion;
    }

    //cout << a;

    cout << "Menu" << endl
         << "\t1. Opcion 1" << endl
         << "\t2. Opcion 2" << endl
         << "\t3. Opcion 3" << endl
         << "Seleccione una opcion: ";

    cin >> seleccion;

    /*if (seleccion == 1)
    {
        cout << "Seleccionaste la opcion 1";
    }
    else if (seleccion == 2)
    {
        cout << "Seleccionaste la opcion 2";
    }
    else if (seleccion == 3)
    {
        cout << "Seleccionaste la opcion 3";
    }
    else
    {
        cout << "A caso eres tonto? Opcion no valida.";
    }*/


    switch (seleccion)
    {
    case 1:
    {
        int a =10;
        
    }
        cout << "Seleccionaste la opcion 1";
        break;
    case 2:
        cout << "Seleccionaste la opcion 2";
        break;
    case 3:
        cout << "Seleccionaste la opcion 3";
        break;
    default:
        cout << "A caso eres tonto? Opcion no valida.";
        //break;
    }
    return 0;
}
