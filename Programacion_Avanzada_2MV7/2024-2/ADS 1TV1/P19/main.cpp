/**
 * @file main.cpp
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief
 * @version 0.1
 * @date 2024-04-22
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream archivo("archivo.txt");
    string variable;

    if (!archivo.is_open())
    {
        ofstream archi("archivo.txt");
        if (!archi.is_open())
        {
            cout << "No fue posible abrir el archivo.";
            return 1;
        }
        archi.close();
    }


    while(!archivo.eof()) {
        getline(archivo, variable);
        //archivo >> variable;
        cout << variable << endl;
    }

    archivo.close();

    return 0;
}
