/**
 * @file factorial.cpp
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Programa que calcula factoriales
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
    cout<< "Usuario, ingrese un numero: ";
    cin >> numero;

    if(numero < 0) {
        cout << "Eres tonto? >:|" << endl;
        return 0;
    }

    if(numero == 0) {
        cout << "El factorial es: 1" << endl;
        return 0;
    }


    for (int i = 1; i <= numero; i++)
    {
        factorial *= i;
    }

    cout << "El factorial es: " << factorial << endl;
    
    return 0;
}
