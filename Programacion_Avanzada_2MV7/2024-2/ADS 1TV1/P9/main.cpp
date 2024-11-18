/**
 * @file main.cpp
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Ejemplo de biblioteca de funciones
 * @version 0.1
 * @date 2024-03-21
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <iostream>
#include <ctime>
#include <cstdlib>
#include "biblioteca.hpp"
#define N 10

using namespace std;

int main()
{
    int arr[N];
    srand(time(NULL));

    for (int i = 0; i < N; i++)
    {
        arr[i] = (rand() % 251) + 50;
    }

    imprime(arr, N);

    burbuja(arr, N);

    imprime(arr, N);

    return 0;
}
