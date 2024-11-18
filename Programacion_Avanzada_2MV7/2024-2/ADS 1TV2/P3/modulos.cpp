/**
 * @file modulos.cpp
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Suma de modulos
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
    int n, suma = 0;
    cout << "Usuario, ingrese un entero positivo mayor a 0: ";
    cin >> n;

    while(n > 0) {
        suma += (n%10);
        //cout << n%10 << endl;
        n /= 10;
    }

    cout << "La suma es: " << suma << endl;
    return 0;
}
