/**
 * @file main.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Manejo de arreglos
 * @version 0.1 
 * @date 2024-03-20
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include "bliblioteca.h"
#define N 10

int main()
{
    int arr[N];
    srand(time(NULL));

    for (int i = 0; i < N; i++)
    {
        arr[i] = rand() % 51;
    }

    imprime(arr, N);
    burbuja(arr, N);
    imprime(arr, N);

    return 0;
}
