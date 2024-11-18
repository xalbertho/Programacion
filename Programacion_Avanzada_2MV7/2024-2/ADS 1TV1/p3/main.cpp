/**
 * @file main.cpp
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Ejemplo del operador ternario
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

    cout << "Usuario, ingrese un numero mayor a 0: ";
    cin >> numero;

    cout << "El numero es " << ((numero & 1) == 0 ? "PAR" : "IMPAR") << endl;
    return 0;
}
