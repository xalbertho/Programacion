/**
 * @file main2.cpp
 * @author your name (you@domain.com)
 * @brief Ejemplo de entradas y salidas
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
    char nom[50];

    
    cout << "Ahora, ingrese su nombre completo: ";
    //getline(cin, nombre);
    cin.getline(nom, 50);

    cout << "Usuario, ingrese su edad: ";
    cin >> edad;

    cout << "Hola " << nom << ", ";
    cout << "su edad es: " << edad << endl;
    
    return 0;
}
