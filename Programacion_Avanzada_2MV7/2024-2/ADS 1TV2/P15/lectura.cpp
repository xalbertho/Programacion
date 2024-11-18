/**
 * @file lectura.cpp
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
    string linea;
    if (!archivo.is_open())
    {
        cout << "No se encontro el archivo.";
        return 1;
    }

    while(!archivo.eof()) {
        //getline(archivo, linea);
        archivo >> linea;
        cout << linea << endl;
    }

    archivo.close();

    return 0;
}
