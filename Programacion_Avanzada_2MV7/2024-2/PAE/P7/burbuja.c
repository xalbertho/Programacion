/**
 * @file burbuja.c
 * @author Jose Luis Cruz (jlcruz@ipn.mx)
 * @brief Ejemplo de la burbuja, bonbon y bellota
 * @version 0.1
 * @date 2024-03-06
 *
 * @copyright Copyright (c) 2024
 *
 */
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define N 1500

int main()
{
    int arr[N], aux;
    srand(time(NULL));

    for (int i = 0; i < N; i++)
    {
        arr[i] = rand() % 100;
    }

    for (int i = 0; i < N; i++)
    {
        printf("%i ", arr[i]);
    }

    for (int j = 0; j < N; j++)
    {
        for (int i = 0; i < N - 1 - j; i++)
        {
            if (arr[i] > arr[i + 1])
            {
                aux = arr[i + 1];
                arr[i + 1] = arr[i];
                arr[i] = aux;
            }
        }
    }

    printf("\n");
    for (int i = 0; i < N; i++)
    {
        printf("%i ", arr[i]);
    }

    return 0;
}
