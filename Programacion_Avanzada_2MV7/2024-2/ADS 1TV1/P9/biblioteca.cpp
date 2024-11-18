/**
 * @file biblioteca.cpp
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Mi biblioteca de funciones chidas
 * @version 0.1
 * @date 2024-03-21 
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <iostream>

using namespace std;

void burbuja(int *arr, int size)
{
    int aux;
    for (int j = 0; j < size; j++)
    {
        for (int i = 0; i < size - 1 - j; i++)
        {
            if (arr[i] > arr[i + 1])
            {
                aux = arr[i];
                arr[i] = arr[i + 1];
                arr[i + 1] = aux;
            }
        }
    }
}

void imprime(int *arr, int size)
{
    cout << "[ ";
    for (int i = 0; i < size; i++)
    {
        cout << arr[i] << " ";
    }
    cout << "]\n";
}
