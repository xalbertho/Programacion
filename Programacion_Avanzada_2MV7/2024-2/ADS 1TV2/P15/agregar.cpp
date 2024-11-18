/**
 * @file agregar.cpp
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief 
 * @version 0.1
 * @date 2024-04-22
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<iostream>
#include<fstream>

using namespace std;

int main()
{
    fstream archivo("archivo.txt", ios::app);

    if(!archivo.is_open()) {
        cout << "No fue posible abrir el archivo.";
        return 1;
    }

    archivo << "Esta linea deberia agregarse hasta el final" << endl;

    archivo.close();

    return 0;
}
