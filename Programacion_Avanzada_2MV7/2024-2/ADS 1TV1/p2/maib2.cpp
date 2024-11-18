/**
 * @file maib2.cpp
 * @author your name (you@domain.com)
 * @brief 
 * @version 0.1
 * @date 2024-03-04
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<iostream>

using namespace std;

int main()
{
    int edad;
    string nombre;

    cout << "Ahora, ingrese su nombre completo: ";
    getline(cin, nombre);
    
    cout << "Usuario, ingrese su edad: ";
    cin >> edad;

    

    cout << "Hola " << nombre << ", ";
    cout << "tu edad es " << edad << endl;

    return 0;
}
