/**
 * @file main3.cpp
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief 
 * @version 0.1
 * @date 2024-03-05
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include<iostream>

using namespace std;

int main()
{
    int var1, suma=0, n;
    float promedio;

    cout << "Querido usuario, ingrese la cantidad de numero a promediar: ";
    cin >> n;

    if(n <= 0) {
        cout << "A caso eres tonto? >:|";
        return 0;
    }

    for (int i = 0; i < n; i++)
    {
        cout << "Ingrese dato " << i+1 << ": ";
        cin >> var1;
        suma+=var1;
    }
    promedio = (float)suma / (float)n;

    cout << "El promedio es: " << promedio;
    
    return 0;
}
