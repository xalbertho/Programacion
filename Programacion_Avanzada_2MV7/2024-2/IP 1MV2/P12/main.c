/**
 * @file main.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Ejemplo
 * @version 0.1 
 * @date 2024-03-21
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "funciones.h"
#define N 10

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
