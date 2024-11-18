/**
 * @file main.cpp
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Ejemplo dle operador ternario
 * @version 0.1
 * @date 2024-03-05
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <iostream>
using namespace std;

int main()
{
    int numero;

    cout << "Usuario, ingrese un entero positivo: ";
    cin >> numero;

    cout << "El numero es " << ((numero & 1) == 1 ? "IMPAR" : "PAR") << endl;
    return 0;
}
