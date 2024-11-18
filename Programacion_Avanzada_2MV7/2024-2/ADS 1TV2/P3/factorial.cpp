/**
 * @file factorial.cpp
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Programa que calcula un factorial
 * @version 0.1
 * @date 2024-03-07
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<iostream>

using namespace std;

int main()
{
    int numero, factorial = 1;
    cout << "Usuario, ingrese un numero entero: ";
    cin >> numero;

    for (int i = 1; i <= numero; i++)
    {
        factorial *= i;
    }

    cout << "El factorial de " << numero << " es: " << factorial << endl;
    
    return 0;
}
