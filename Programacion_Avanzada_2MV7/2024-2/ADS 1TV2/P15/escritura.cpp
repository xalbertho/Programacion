/**
 * @file escritura.cpp
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
    ofstream archivo("archivo.txt");
    if(!archivo.is_open()) {
        cout << "No fue posible crear el archivo.";
        return 1;
    }

    archivo << "Hola a todos" << endl;
    archivo << "Esto es una prueba de escritura" << endl;

    archivo.close();


    return 0;
}
