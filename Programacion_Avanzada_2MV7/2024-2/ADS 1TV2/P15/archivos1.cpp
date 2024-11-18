/**
 * @file archivos1.cpp
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

    if (!archivo.is_open())
    {
        // Intentamos crearlo
        ofstream archi("archivo.txt");
        if (!archi.is_open())
        {
            cout << "No fue posible encontrar el archivo." << endl;
            return 1;
        }
        archi.close();
    }

    archivo.close();
    return 0;
}
